//画像アップロードのフォーム部品

const after_bg_color = 'rgb(49 49 49)';
const after_bg_radius = '10px'

$(document).on('change', '#id_post_image1', function(){
        if (!this.files.length) {
            console.log("false")
            return;
        }
        console.log("true")
        var file = $(this).prop('files')[0];
        var fr = new FileReader();
        $('#img_post1').css('background-image', 'none');
        fr.onload = function() {
            $('#img_post1').css('background-image', 'url(' + fr.result + ')');
            $('#img_post1').css('background-color', after_bg_color);
            $('#img_post1').css('border-radius', after_bg_radius);
        }
        fr.readAsDataURL(file);
        $("#img_post1 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image2', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post2').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post2').css('background-image', 'url(' + fr.result + ')');
        $('#img_post2').css('background-color', after_bg_color);
        $('#img_post2').css('border-radius', after_bg_radius);
    }
    fr.readAsDataURL(file);
    $("#img_post2 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image3', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post3').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post3').css('background-image', 'url(' + fr.result + ')');
        $('#img_post3').css('background-color', after_bg_color);
        $('#img_post3').css('border-radius', after_bg_radius);
    }
    fr.readAsDataURL(file);
    $("#img_post3 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image4', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post4').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post4').css('background-image', 'url(' + fr.result + ')');
        $('#img_post4').css('background-color', after_bg_color);
        $('#img_post4').css('border-radius', after_bg_radius);
    }
    fr.readAsDataURL(file);
    $("#img_post4 img").css('opacity', 0);
});

// 地区町村メニューの設定
// main.js
$(function() {
    $('#id_prefectures').on('change', function() {
      var SelectedPrefectureDropdown = $(this).children("option:selected"); 
      var SelectedPrefectureText = SelectedPrefectureDropdown.text();
      $.ajax({
        url: '/get_area_dropdown/',
        data: {
          'prefectures_text': SelectedPrefectureText
        },
        dataType: 'json',
        success: function(data) {
          var AreaDropdownChoices = data.area_dropdown_choices;
          var AreaDropdown = $('#id_area');
          
          AreaDropdown.empty();
          $.each(AreaDropdownChoices, function(index, value) {
            AreaDropdown.append($('<option>').text(value.area_name).val(value.id));
          });
        }
      });
    });
  });
  
  