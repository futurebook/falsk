var captchaBtn = document.getElementById("captcha-btn");

//ajax请求
var Ajax = {
        get: function (url, callback) {
            // XMLHttpRequest对象用于在后台与服务器交换数据
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, false);
            xhr.send(null);
            return xhr.status;
        },

        // data应为'a=a1&b=b1'这种字符串格式，在jq里如果data为对象会自动将对象转成这种字符串格式
        post: function (url, data, callback) {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', url, false);
            // 添加http头，发送信息至服务器时内容编码类型
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {
                    if (xhr.status == 200 || xhr.status == 304) {
                        // console.log(xhr.responseText);
                        // return JSON.parse(xhr.responseText);
                        callback(xhr.responseText);
                    }
                }
            }
            xhr.send(data);
        }
    }

//倒计时限制秒数
var countdown = 30;
var id;//该变量用作停止定时执行函数
function setTime(targetElement) {
    if (countdown == 0) {
        targetElement.removeAttribute("disabled");
        targetElement.innerHTML = "获取验证码";
        countdown = 30;
        clearTimeout(id);//关闭定时执行函数
    } else {
        targetElement.setAttribute("disabled", true);
        targetElement.innerHTML = "重新发送(" + countdown + ")";
        countdown--;
        id = setTimeout(function () {
            setTime(targetElement)
        }, 1000);//下次定时调用setTime
    }
}

captchaBtn.onclick = function () {
    var i = document.getElementById("exampleInputEmail1");
    var email = i.value;
    var check_email = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
    if (email){
        if (check_email.test(email)){
            var res = Ajax.post("/user/captcha/", email);
            if (res) {
                alert(res["message"]);
            }
            setTime(this);
        }else {
            alert('邮箱格式错误！');
        }
    }else {
        alert("请填写邮箱！");
    }
}







