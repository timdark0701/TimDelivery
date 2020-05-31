// $(document).ready(function() {
//     $('.add_to_cart').on('click', function (e) {
//         e.preventDefault();
//         food_slug = $(this).attr('data-slug');
//         console.log(1);
//         $.ajax({
//             type: "GET",
//             url: '{% url 'cart:cart_add' %}',
//             data: {
//                 'food_slug': food_slug,
//             },
//             dataType: 'json',
//             success: function (data) {
//                 $('#cart_count').html(data.cart_quantity)
//             }
//         })
//     })
// })