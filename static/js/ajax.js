$(document).ready(function () {
    $('body').on('submit', '#form_buying_plant', function (e) {
        e.preventDefault();
        let form = $(this);
        var form_plant_id = form.data('plant_id');
        $.ajax({
            url: form.attr("action"),
            type: 'get',
            data: { 'form_plant_id': form_plant_id },
            cache: true,
            success: function (request) {
                $('#total_qty').text(request.message1);
                console.log(request.message2[form_plant_id])
                if (request.message2[form_plant_id] == request.message) {
                    $('button[type="submit"]', form).prop('disabled', true).css('background-color', 'lightgray');
                } else {
                    $('button[type="submit"]', form).prop('disabled', false).css('background-color', '');
                }
            },
            error: function () {
                console.log('error');
            }
        });

    })

})




