import { Injectable } from '@angular/core';

import { TranslateService } from '@ngx-translate/core';

import { ConstantsService } from 'app/core/core-services/constants.service';
import { AssignmentPollRepositoryService } from 'app/core/repositories/assignments/assignment-poll-repository.service';
import { ConfigService } from 'app/core/ui-services/config.service';
import {
    AssignmentPoll,
    AssignmentPollMethod,
    AssignmentPollPercentBase
} from 'app/shared/models/assignments/assignment-poll';
import { MajorityMethod, PollType, VOTE_UNDOCUMENTED } from 'app/shared/models/poll/base-poll';
import { ParsePollNumberPipe } from 'app/shared/pipes/parse-poll-number.pipe';
import { PollKeyVerbosePipe } from 'app/shared/pipes/poll-key-verbose.pipe';
import { ViewAssignmentOption } from 'app/site/assignments/models/view-assignment-option';
import { ViewAssignmentPoll } from 'app/site/assignments/models/view-assignment-poll';
import {
    PollData,
    PollDataOption,
    PollService,
    PollTableData,
    VotingResult
} from 'app/site/polls/services/poll.service';

@Injectable({
    providedIn: 'root'
})
export class AssignmentPollService extends PollService {

    private static sumOptionsYN(poll: PollData): number {
        return poll.options.reduce((t, o) => {
            if (t >= 0 && o.yes >= 0 && o.no >= 0) {
                t += o.yes + o.no;
                return t;
            }
            return -1; // yes or no < 0
        }, 0);
    }

    private static sumOptionsYNA(poll: PollData): number {
        return poll.options.reduce((t, o) => {
            if (t >= 0 && o.yes >= 0 && o.no >= 0 && o.abstain >= 0) {
                t += o.yes + o.no + o.abstain;
                return t;
            }
            return -1; // yes, no, or abstain < 0
        }, 0);
    }

    /**
     * The default percentage base
     */
    public defaultPercentBase: AssignmentPollPercentBase;

    /**
     * The default majority method
     */
    public defaultMajorityMethod: MajorityMethod;

    public defaultGroupIds: number[];

    public defaultPollMethod: AssignmentPollMethod;

    public defaultPollType: PollType;

    private sortByVote: boolean;

    /**
     * Constructor. Subscribes to the configuration values needed
     * @param config ConfigService
     */
    public constructor(
        config: ConfigService,
        constants: ConstantsService,
        pollKeyVerbose: PollKeyVerbosePipe,
        parsePollNumber: ParsePollNumberPipe,
        protected translate: TranslateService,
        private pollRepo: AssignmentPollRepositoryService
    ) {
        super(config, constants, translate, pollKeyVerbose, parsePollNumber);
        config
            .get<AssignmentPollPercentBase>('assignment_poll_default_100_percent_base')
            .subscribe(base => (this.defaultPercentBase = base));
        config
            .get<MajorityMethod>('assignment_poll_default_majority_method')
            .subscribe(method => (this.defaultMajorityMethod = method));
        config.get<number[]>(AssignmentPoll.defaultGroupsConfig).subscribe(ids => (this.defaultGroupIds = ids));
        config
            .get<AssignmentPollMethod>(AssignmentPoll.defaultPollMethodConfig)
            .subscribe(method => (this.defaultPollMethod = method));
        config.get<PollType>('assignment_poll_default_type').subscribe(type => (this.defaultPollType = type));
        config.get<boolean>('assignment_poll_sort_poll_result_by_votes').subscribe(sort => (this.sortByVote = sort));
    }

    public getDefaultPollData(contextId?: number): AssignmentPoll {
        const poll = new AssignmentPoll({
            ...super.getDefaultPollData()
        });

        poll.title = this.translate.instant('Ballot');
        poll.pollmethod = this.defaultPollMethod;

        if (contextId) {
            const length = this.pollRepo.getViewModelList().filter(item => item.assignment_id === contextId).length;
            if (length) {
                poll.title += ` (${length + 1})`;
            }
        }

        return poll;
    }

    private getGlobalVoteKeys(poll: ViewAssignmentPoll | PollData): VotingResult[] {
        return [
            {
                vote: 'amount_global_no',
                showPercent: this.showPercentOfValidOrCast(poll),
                hide: poll.amount_global_no === VOTE_UNDOCUMENTED || !poll.amount_global_no
            },
            {
                vote: 'amount_global_abstain',
                showPercent: this.showPercentOfValidOrCast(poll),
                hide: poll.amount_global_abstain === VOTE_UNDOCUMENTED || !poll.amount_global_abstain
            }
        ];
    }

    public generateTableData(poll: ViewAssignmentPoll | PollData): PollTableData[] {
        const tableData: PollTableData[] = poll.options
            .sort((a, b) => {
                if (this.sortByVote) {
                    return b.yes - a.yes;
                } else {
                    // PollData does not have weight, we need to rely on the order of things.
                    if (a.weight && b.weight) {
                        return b.weight - a.weight;
                    }
                }
            })
            .map((candidate: ViewAssignmentOption) => {
                const pollTableEntry: PollTableData = {
                    class: 'user',
                    value: super.getVoteTableKeys(poll).map(
                        key =>
                            ({
                                vote: key.vote,
                                amount: candidate[key.vote],
                                icon: key.icon,
                                hide: key.hide,
                                showPercent: key.showPercent,
                                candidateId: candidate.user_id
                            } as VotingResult)
                    )
                };

                // Since pollData does not have any subtitle option
                if (candidate instanceof ViewAssignmentOption) {
                    pollTableEntry.votingOption = candidate.user.short_name;
                    pollTableEntry.votingOptionSubtitle = candidate.user.getLevelAndNumber();
                } else {
                    pollTableEntry.votingOption = (candidate as PollDataOption).user.short_name;
                }

                return pollTableEntry;
            });
        tableData.push(...this.formatVotingResultToTableData(this.getGlobalVoteKeys(poll), poll));
        tableData.push(...this.formatVotingResultToTableData(super.getSumTableKeys(poll), poll));
        return tableData;
    }

    private formatVotingResultToTableData(resultList: VotingResult[], poll: PollData): PollTableData[] {
        return resultList
            .filter(key => {
                return !key.hide;
            })
            .map(key => ({
                votingOption: key.vote,
                class: 'sums',
                value: [
                    {
                        amount: poll[key.vote],
                        hide: key.hide,
                        showPercent: key.showPercent
                    } as VotingResult
                ]
            }));
    }

    public getPercentBase(poll: PollData, candidateId: number): number {
        const base: AssignmentPollPercentBase = poll.onehundred_percent_base as AssignmentPollPercentBase;
        let totalByBase: number;
        let option: PollDataOption;
        switch (base) {
            case AssignmentPollPercentBase.YN:
                if (candidateId) {
                    // 100% percent base is sum of YN of the candidate.
                    option = poll.options.find(o => o.user.id === candidateId);
                    totalByBase = option.yes >= 0 && option.no >= 0 ?
                        option.yes + option.no : -1;
                } else {
                    // 100% base is sum of YN of all candidates.
                    totalByBase = AssignmentPollService.sumOptionsYN(poll);
                }
                break;
            case AssignmentPollPercentBase.YNA:
                if (candidateId) {
                    // 100% percent base is sum of YNA of the candidate.
                    option = poll.options.find(o => o.user.id === candidateId);
                    totalByBase = option.yes >= 0 && option.no >= 0 && option.abstain >= 0 ?
                        option.yes + option.no + option.abstain : -1;
                } else {
                    // 100% base is sum of YNA of all candidates.
                    totalByBase = AssignmentPollService.sumOptionsYNA(poll)
                }
                break;
            case AssignmentPollPercentBase.Votes:
                // 100% base is sum of YNA of all candidates.
                totalByBase = AssignmentPollService.sumOptionsYNA(poll);
                break;
            case AssignmentPollPercentBase.Valid:
                totalByBase = poll.votesvalid;
                break;
            case AssignmentPollPercentBase.Cast:
                totalByBase = poll.votescast;
                break;
            default:
                break;
        }
        return totalByBase;
    }

    public getChartLabels(poll: PollData): string[] {
        const fields = this.getPollDataFields(poll);
        return poll.options.map(option => {
            const votingResults = fields.map(field => {
                const voteValue = option[field];
                const votingKey = this.translate.instant(this.pollKeyVerbose.transform(field));
                const resultValue = this.parsePollNumber.transform(voteValue);
                const resultInPercent = this.getVoteValueInPercent(voteValue, poll);
                let resultLabel = `${votingKey}: ${resultValue}`;

                // 0 is a valid number in this case
                if (resultInPercent !== null) {
                    resultLabel += ` (${resultInPercent})`;
                }
                return resultLabel;
            });

            return `${option.user.short_name} · ${votingResults.join(' · ')}`;
        });
    }
}
