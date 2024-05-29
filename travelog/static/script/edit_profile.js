// 初期表示時はCroppieを非表示
$('#profileImage_croppie').ready(function(event){
    $('#profileImage_croppie').css('display','none');
});

$(document).ready(function(){
    var content_width = window.innerWidth
    var content_height = content_width
    viewportWidth = content_width * 0.7 //クロッピングするサイズ（横幅 ピクセル表記）
    viewportHeight = content_height * 0.7 //クロッピングするサイズ（縦幅 ピクセル表記）
    boundaryWidth = content_width * 0.8 //クロッピング元画像のサイズ（横幅 ピクセル表記）
    boundaryHeight = content_height * 0.8 //クロッピング元画像のサイズ（縦幅 ピクセル表記）

    // croppieの初期設定
    $image_crop = $('#profileImage_croppie').croppie({
        enableExif: true,
        viewport: {
            width: viewportWidth,
            height: viewportHeight,
            type:'circle' //円形にクロッピングしたい際はここをcircleとする
        },
        boundary: {
            width: boundaryWidth,
            height: boundaryHeight
        }
    })

    $('#id_profile_img').on('change', function(){
        var reader = new FileReader();
        reader.onload = function (event) {
            $image_crop.croppie('bind', {
                url: event.target.result
            }).then(function(){
                // console.log('Bind complete');
            });
        }
        $('#profileImage_croppie').css('display','block');
        $('#profileImage_croppie').css('height','auto');
        $('#profileImage_croppie').css('margin-top','2rem');
        reader.readAsDataURL(this.files[0]);
    })

    // 保存ボタン押下
$('form').on('submit', function(ev) {
    ev.preventDefault();
    $image_crop.croppie('result', {
        type: 'base64',
        size: { width: 150, height: 150 }
    }).then(function(base64) {
        $('#profile_img_data').val(base64);
        ev.currentTarget.submit();
    });
});
});