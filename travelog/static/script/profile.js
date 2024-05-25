$('#follow_button').on('click', function() {
    var $btn = $(this);
    var to_follow_id = $btn.val(); // jQueryオブジェクトから値を取得
    console.log("押しました");
    $.ajax({
        url: '/follow_user/' + to_follow_id,
        method: 'POST', // HTTPメソッドを指定（適宜変更）
        cache: false, // キャッシュバスティング
        success: function() { 
            if ($btn.text().trim() === 'フォローする') {
                $btn.text('フォロー中');
            } else {
                $btn.text('フォローする');
            }
        },
        error: function() {
            // 通信失敗時の処理を記述
            alert("通信に失敗しました。もう一度お試しください。");
        }
    });
});
