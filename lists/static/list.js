window.Superlists = {};
window.Superlists.initialize = function () {
    $('input[name="text"]').on('focusin', function () {
         $('#invalid-message').hide();
    });
};