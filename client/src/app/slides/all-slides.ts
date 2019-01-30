import { SlideManifest } from './slide-manifest';

/**
 * Here, all slides has to be registered.
 *
 * Note: When adding or removing slides here, you may need to restart yarn/npm, because
 * the angular CLI scans this file just at it's start time and creates the modules then. There
 * is no such thing as "dynamic update" in this case..
 */
export const allSlides: SlideManifest[] = [
    {
        slide: 'motions/motion',
        path: 'motions/motion',
        loadChildren: './slides/motions/motion/motions-motion-slide.module#MotionsMotionSlideModule',
        scaleable: true,
        scrollable: true,
        verboseName: 'Motion',
        elementIdentifiers: ['name', 'id'],
        canBeMappedToModel: true
    },
    {
        slide: 'users/user',
        path: 'users/user',
        loadChildren: './slides/users/user/users-user-slide.module#UsersUserSlideModule',
        scaleable: true,
        scrollable: true,
        verboseName: 'Participant',
        elementIdentifiers: ['name', 'id'],
        canBeMappedToModel: true
    },
    {
        slide: 'core/clock',
        path: 'core/clock',
        loadChildren: './slides/core/clock/core-clock-slide.module#CoreClockSlideModule',
        scaleable: false,
        scrollable: false,
        verboseName: 'Clock',
        elementIdentifiers: ['name'],
        canBeMappedToModel: false
    },
    {
        slide: 'core/countdown',
        path: 'core/countdown',
        loadChildren: './slides/core/countdown/core-countdown-slide.module#CoreCountdownSlideModule',
        scaleable: false,
        scrollable: false,
        verboseName: 'Countdown',
        elementIdentifiers: ['name', 'id'],
        canBeMappedToModel: true
    },
    {
        slide: 'agenda/current-list-of-speakers',
        path: 'agenda/current-list-of-speakers',
        loadChildren:
            './slides/agenda/current-list-of-speakers/agenda-current-list-of-speakers-slide.module#AgendaCurrentListOfSpeakersSlideModule',
        scaleable: true,
        scrollable: true,
        verboseName: 'Current list of speakers',
        elementIdentifiers: ['name', 'id'],
        canBeMappedToModel: false
    },
    {
        slide: 'agenda/current-list-of-speakers-overlay',
        path: 'agenda/current-list-of-speakers-overlay',
        loadChildren:
            './slides/agenda/current-list-of-speakers-overlay/agenda-current-list-of-speakers-overlay-slide.module#AgendaCurrentListOfSpeakersOverlaySlideModule',
        scaleable: false,
        scrollable: false,
        verboseName: 'Current list of speakers overlay',
        elementIdentifiers: ['name', 'id'],
        canBeMappedToModel: false
    }
];