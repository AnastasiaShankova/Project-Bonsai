$(document).ready(function () {
    $('body').on('click', '#oneminus', function (e) {
        e.preventDefault();
        let a = $(this);
        var a_basket_id = a.data('basket_id')
        var a_basket_qty = a.data('basket_quantity')
        var a_sign = a.data('sign')
        var url = a.attr("href")
        console.log(a)
        console.log(a_basket_id)
        console.log(a_sign)
        console.log(a_basket_qty)
        console.log(url)

        $.ajax({
            url: a.attr("href"),
            type: 'get',
            data: { 'a_basket_id': a_basket_id, 'a_sign': a_sign, 'a_basket_qty': a_basket_qty, },
            cache: true,
            success: function (request) {
                $('#total_qty').text(request.message);
                console.log(a_basket_id)
                $(a_basket_id).text(request.message1);
                if (request.message1 == 0) {
                }

                // if (request.message2[form_plant_id] == request.message) {
                //     $('button[type="submit"]', form).prop('disabled', true).css('background-color', 'lightgray');
                // } else {
                //     $('button[type="submit"]', form).prop('disabled', false).css('background-color', '');
                // }
            },
            error: function () {
                console.log('error');
            }
        });





    })
})