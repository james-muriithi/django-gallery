$(function () {
    $('.modal').appendTo("body")
    
    $('[data-bs-toggle="tooltip"]').tooltip()

    $('.share').on('click', function () {
        const url = $(this).data('url')
        const title = $(this).attr('title')
        if (navigator.share) {
            navigator.share({
                title,
                text: url,
                url
            }).then(() => {
                showCopiedTooltip($(this))
            }).catch(err => {
                console.log(`Couldn't share because of`, err.message);
            });
        } else {
            navigator.clipboard.writeText(url);
            showCopiedTooltip($(this))
        }
    })
});

const showCopiedTooltip = function (element, delay = 3000) {
    element.attr('data-bs-original-title', 'Url copied!')
    element.tooltip("show")
    setTimeout(() => {
        element.attr('data-bs-original-title', 'Copy image url')
        element.tooltip("hide")
    }, delay)
}