(function () {

'use strict';

angular.module('OpenSlidesApp.poll.majority', [])

.value('MajorityMethodChoices', [
    {'value': 'simple_majority', 'display_name': 'Simple majority'},
    {'value': 'two-thirds_majority', 'display_name': 'Two-thirds majority'},
    {'value': 'three-quarters_majority', 'display_name': 'Three-quarters majority'},
    {'value': 'disabled', 'display_name': 'Disabled'},
])

.factory('MajorityMethods', [
    function () {
        return {
            'simple_majority': function (vote, base, precision) {
                var factor = Math.pow(10, precision);
                return (Math.ceil(-(base / 2 - vote) * factor) - 1) / factor;
            },
            'two-thirds_majority': function (vote, base, precision) {
                var factor = Math.pow(10, precision);
                var result = -(base * 2 - vote * 3) * factor / 3;
                if (result % 1 !== 0) {
                    result = Math.ceil(result) - 1;
                }
                return result / factor;
            },
            'three-quarters_majority': function (vote, base, precision) {
                var factor = Math.pow(10, precision);
                var result = -(base * 3 - vote * 4) * factor / 4;
                if (result % 1 !== 0) {
                    result = Math.ceil(result) - 1;
                }
                return result / factor;
            },
            'disabled': function () {
                return undefined;
            },
        };
    }
]);

}());
