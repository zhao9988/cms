init();
var  userName;
var pwd;
function init() {

	ajax();
}

function ajax() {
    $("form").validate({
        rules:{
                username:{
                    required:true,
                    minlength:2,
                    maxlength:10
                },
                pwd:{
                    required:true,
                }
                },
        submitHandler:function(form){
            alert("验证成功不提交");
        $("form").ajaxSubmit(function (data) {
            //后端返回的数据
            alert(data);
            setStordge()
        })
        }
    })
}
function setStordge() {
    userName = $(".username").val();
    pwd = $(".pwd").val();
    var userObj={
        name:userName,
        pwd:pwd
    };
    //格式是个列表
    var storage = JSON.parse(localStorage.getItem("user"));
    console.log(storage)
        if (storage == null) {
            storage = []
        } else {
            for (var i = 0; i < storage.length; i++) {
                if (userName == storage[i]["name"]) {//如果重复不操作
                    alert("当前用户名已存在")
                    return;
                }
            }
        }
        // alert(userName);
        // alert(storage);

        storage.push(userObj);
        localStorage.setItem("user", JSON.stringify(storage))
        location.href="http://127.0.0.1:8000/login/"

}


