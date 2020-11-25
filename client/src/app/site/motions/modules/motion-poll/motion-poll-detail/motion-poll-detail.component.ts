import { ChangeDetectionStrategy, Component, ViewEncapsulation } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute, Router } from '@angular/router';

import { TranslateService } from '@ngx-translate/core';
import { PblColumnDefinition } from '@pebula/ngrid';

import { OperatorService, Permission } from 'app/core/core-services/operator.service';
import { MotionPollRepositoryService } from 'app/core/repositories/motions/motion-poll-repository.service';
import { MotionVoteRepositoryService } from 'app/core/repositories/motions/motion-vote-repository.service';
import { GroupRepositoryService } from 'app/core/repositories/users/group-repository.service';
import { ConfigService } from 'app/core/ui-services/config.service';
import { PromptService } from 'app/core/ui-services/prompt.service';
import { ViewMotion } from 'app/site/motions/models/view-motion';
import { ViewMotionPoll } from 'app/site/motions/models/view-motion-poll';
import { MotionPollDialogService } from 'app/site/motions/services/motion-poll-dialog.service';
import { MotionPollService } from 'app/site/motions/services/motion-poll.service';
import { BasePollDetailComponentDirective } from 'app/site/polls/components/base-poll-detail.component';
import { MotionPollPdfService } from "../../../services/motion-poll-pdf.service";

@Component({
    selector: 'os-motion-poll-detail',
    templateUrl: './motion-poll-detail.component.html',
    styleUrls: ['./motion-poll-detail.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
    encapsulation: ViewEncapsulation.None
})
export class MotionPollDetailComponent extends BasePollDetailComponentDirective<ViewMotionPoll, MotionPollService> {
    public motion: ViewMotion;
    public columnDefinition: PblColumnDefinition[] = [
        {
            prop: 'user',
            width: 'auto',
            label: 'Participant'
        },
        {
            prop: 'vote',
            width: 'auto',
            label: 'Vote'
        }
    ];

    public filterProps = ['user.getFullName', 'valueVerbose'];

    public isVoteWeightActive: boolean;

    protected get hasPerms(): boolean {
        return this.operator.hasPerms(Permission.motionsCanManagePolls);
    }

    public constructor(
        title: Title,
        translate: TranslateService,
        matSnackbar: MatSnackBar,
        repo: MotionPollRepositoryService,
        route: ActivatedRoute,
        groupRepo: GroupRepositoryService,
        prompt: PromptService,
        pollDialog: MotionPollDialogService,
        pollService: MotionPollService,
        private pdfService: MotionPollPdfService,
        votesRepo: MotionVoteRepositoryService,
        configService: ConfigService,
        protected operator: OperatorService,
        private router: Router
    ) {
        super(
            title,
            translate,
            matSnackbar,
            repo,
            route,
            groupRepo,
            prompt,
            pollDialog,
            pollService,
            votesRepo,
            operator
        );
        configService
            .get<boolean>('users_activate_vote_weight')
            .subscribe(active => (this.isVoteWeightActive = active));
    }

    public downLoadPdf(): void {
        this.pdfService.exportSingleVotes(this.poll, this.isVoteWeightActive);
    }

    protected createVotesData(): void {
        this.setVotesData(this.poll.options[0].votes);
    }

    protected onDeleted(): void {
        this.router.navigate(['motions', this.poll.motion_id]);
    }
}
