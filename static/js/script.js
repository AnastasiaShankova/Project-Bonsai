// animation for index.html
var text = 'BONSAI.BY';
var content = document.getElementById('index_content');
for (var i in [...text]) {
    var letter = document.createElement('span');
    letter.textContent = [...text][i];
    if (letter.textContent.match(/\s/)) {
        letter.style.margin = 'auto 3px';
    }
    letter.style.animationDelay = i / 10 + 's';
    content.appendChild(letter);
};
var other_text = 'Магазин декоративных растений'
var other_content = document.getElementById('other_content');
for (var i in [...other_text]) {
    var letter = document.createElement('span')
    letter.textContent = [...other_text][i]
    if (letter.textContent.match(/\s/)) {
        letter.style.margin = 'auto 3px'
    }
    letter.style.animationDelay = i / 10 + 's'
    other_content.appendChild(letter)
};
var next_text = 'Растения,'
var next_text_2 = 'которые добавят изюминку в ваш интерьер'
var next_content = document.getElementById('next_content');
var next_content_2 = document.getElementById('next_content_2');
for (var i in [...next_text]) {
    var letter = document.createElement('span')
    letter.textContent = [...next_text][i]
    if (letter.textContent.match(/\s/)) {
        letter.style.margin = 'auto 3px'
    }
    letter.style.animationDelay = i / 10 + 's'
    next_content.appendChild(letter)
};
for (var i in [...next_text_2]) {
    var letter = document.createElement('span')
    letter.textContent = [...next_text_2][i]
    if (letter.textContent.match(/\s/)) {
        letter.style.margin = 'auto 3px'
    }
    letter.style.animationDelay = i / 10 + 's'
    next_content_2.appendChild(letter)
};




//ajax//
// var submit_btn = document.querySelectorAll('button');
// console.log(submit_btn);
// // var plant_id = submit_btn.data('plant_id');
// // var basket_total_qty = total_qty.data('basket_total_qty');

// $(document).ready(function () {
//     // var form = $('#form_buying_plant');
//     var form = document.querySelectorAll('#form_buying_plant');
//     console.log(form);
//     form.on('submit', function (e) {
//         e.preventDefault();
//         console.log('123');
//         // var basket = $('#basket').val();
//         // console.log(basket);
//         // var submit_btn = $('#submit_btn');

//         // var submit_btn = document.querySelectorAll('button');
//         // console.log(submit_btn);
//         // var plant_id = submit_btn.data('plant_id');
//         // var basket_total_qty = total_qty.data('basket_total_qty');


//         console.log(plant_id);

//         console.log(basket_total_qty);



//         var data = {};
//         data.plant_id = plant_id;
//         data.basket_total_qty = basket_total_qty;
//         // data.basket_total_qty = basket_total_qty;
//         console.log(data)

//         var csrf_token = $('#form_buying_plant [name = "csrfmiddlewaretoken"]').val();
//         data["csrfmiddlewaretoken"] = csrf_token;
//         var url = form.attr("action");
//         $.ajax({
//             url: url,
//             tpe: 'POST',
//             data: data,
//             cache: true,
//             success: function (data) {
//                 console.log('ok');
//                 // $('#total_qty').text(basket_total_qty + 1);
//                 basket_total_qty++;
//                 $('#total_qty').text(basket_total_qty);
//             },
//             error: function () {
//                 console.log('error');
//             }
//         });

//         $('basket_item_card').append(plant_id);




//     });
// });




// var submit_btn = document.getElementsByClassName('in_busket_a');
// console.log(submit_btn);
// forEach((element) => console.log(element));



// button.addEventListener("click", function () {
//     alert("egrbg")
// });

// ///////////////////////

// var plant_id
// var basket_total_qty

// const buttons = document.querySelectorAll('button');
// console.log(buttons);
// buttons.forEach(button => {
//     button.addEventListener('click', () => {
//         var form = $(this);
//         var plant_id = button.dataset.plant_id;
//         var basket_total_qty = button.dataset.basket_total_qty;
//         alert(plant_id);
//         return plant_id;
//     });
// });


// var data = {};
// var csrf_token = $('#form_buying_plant [name = "csrfmiddlewaretoken"]').val();
// data["csrfmiddlewaretoken"] = csrf_token;
// var form = $(this);
// var url = form.attr("action");
// $.ajax({
//     url: url,
//     tpe: 'POST',
//     data: data,
//     cache: true,
//     success: function (data) {
//         const buttons = document.querySelectorAll('button');
//         console.log(buttons);
//         buttons.forEach(button => {
//             button.addEventListener('click', () => {
//                 var plant_id = button.dataset.plant_id;
//                 var basket_total_qty = button.dataset.basket_total_qty;
//                 alert(plant_id);
//                 return plant_id;
//             });
//         });
//         console.log('ok');
//         // $('#total_qty').text(basket_total_qty + 1);
//         basket_total_qty++;
//         $('#total_qty').text(basket_total_qty);
//     },
//     error: function () {
//         console.log('error');
//     }
// });

// $('basket_item_card').append(plant_id);



// var form = $(this);
// var plant_id = form.dataset.plant_id;
// alert(plant_id);
// ///////////////////        занятие в чт    /////////////////////////////////////////
// var data = {};

// const buttons = document.querySelectorAll('form');
// console.log(buttons);
// buttons.forEach(button => {
//     a = button.addEventListener('submit', () => {
//         var form = $(this);
//         var plant_id = button.dataset.plant_id;
//         var basket_total_qty = button.dataset.basket_total_qty;
//         alert(plant_id);
//         alert(basket_total_qty);
//         var data = {};
//         data['plant_id'] = plant_id;
//         data['basket_total_qty'] = basket_total_qty;
//         alert(data);
//         // return data
//         alert(data.plant_id)
//     });
// });

// var form = $(this);
// var url = form.attr("action");
// // $.ajax({
// //     url: url,
// //     tpe: 'POST',
// //     data: data,
// //     cache: true,
// //     success: function (data) {
// //         const buttons = document.querySelectorAll('button');
// //         console.log(buttons);
// //         buttons.forEach(button => {
// //             button.addEventListener('click', () => {
// //                 // var plant_id = button.dataset.plant_id;
// //                 // var basket_total_qty = button.dataset.basket_total_qty;
// //                 alert(plant_id);
// //                 return plant_id;
// //             });
// //         });
// //         console.log('ok');
// //         // $('#total_qty').text(basket_total_qty + 1);
// //         data.basket_total_qty++;
// //         $('#total_qty').text(basket_total_qty);
// //     },
// //     error: function () {
// //         console.log('error');
// //     }
// // });

// // $('basket_item_card').append(plant_id);
