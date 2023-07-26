// login
$("a[data-type='btn-login']").click(function (e) {
    e.preventDefault();
    let $tips = $("#tips");
    $.ajax({
        type: "post",
        dataType: "json",
        data: $("#login").serialize(),
        async: true,
        beforeSend: function (xhr) {
            xhr.setRequestHeader(
                "X-CSRFToken",
                $("input[name='csrfmiddlewaretoken']").attr("value")
            );
        },
        success: function (data) {
            $tips.css({"font-weight": "bold"});
            switch (data.status) {
                case "success":
                    $tips.css({"color": "green"})
                    $tips.text("登录成功");
                    setTimeout(function () {
                        window.location.replace()
                    }, 500);
                    break;
                case "failed":
                    $tips.css({"color": "brown"})
                    $tips.text("登录失败，邮箱或密码错误");
                    break;
                case "form":
                    $tips.css({"color": "darkorange"})
                    $tips.text("登录失败，邮箱或密码格式不正确");
            }
        },
        error: function () {
            $tips.css({"color": "red", "font-weight": "bold"})
            $tips.text("未知错误，请查看日志");
        },
    });
})