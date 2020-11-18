import { Injectable } from '@angular/core';

import { TranslateService } from '@ngx-translate/core';

import { OpenSlidesStatusService } from 'app/core/core-services/openslides-status.service';
import { StorageService } from 'app/core/core-services/storage.service';
import { BaseSortListService } from 'app/core/ui-services/base-sort-list.service';
import { OsSortingDefinition, OsSortingOption } from 'app/core/ui-services/base-sort.service';
import { OperatorService } from "../../../core/core-services/operator.service";
import { ViewUser } from '../models/view-user';

/**
 * Sorting service for the user list
 */
@Injectable({
    providedIn: 'root'
})
export class UserSortListService extends BaseSortListService<ViewUser> {
    /**
     * set the storage key name
     */
    protected storageKey = 'UserList';

    /**
     * Define the sort options
     */
    private userSortOptions: OsSortingOption<ViewUser>[] = [
        { property: 'first_name', label: 'Given name' },
        { property: 'last_name', label: 'Surname' },
        { property: 'is_present', label: 'Presence' },
        { property: 'is_active', label: 'Is active' },
        { property: 'is_committee', label: 'Is committee' },
        { property: 'number', label: 'Participant number' },
        { property: 'structure_level', label: 'Structure level' },
        { property: 'vote_weight', label: 'Vote weight' },
        { property: 'comment' }
        // TODO email send?
    ];

    /**
     * Constructor.
     *
     * @param translate required by parent
     * @param store requires by parent
     */
    public constructor(
        translate: TranslateService,
        store: StorageService,
        OSStatus: OpenSlidesStatusService,
        private operator: OperatorService
    ) {
        super(translate, store, OSStatus);
    }

    /**
     * @override
     */
    protected getSortOptions(): OsSortingOption<ViewUser>[] {
        // Non-admins can only sort by name or presence.
        return this.operator.isSuperAdmin ? this.userSortOptions : this.userSortOptions.slice(0, 3);
    }

    /**
     * Required by parent
     *
     * @returns the default sorting strategy
     */
    public async getDefaultDefinition(): Promise<OsSortingDefinition<ViewUser>> {
        return {
            sortProperty: 'first_name',
            sortAscending: true
        };
    }
}
