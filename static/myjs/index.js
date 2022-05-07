// upload Function 
function fileUploadFunc(fileSource, fileSourceName) {
    // console.log(fileSource);
    const fileDetails = JSON.stringify({
        name : fileSourceName
    })
    
    let formData = new FormData();
    formData.append('body', fileDetails)
    formData.append('file', fileSource);

    $.ajax({
        type: "POST",
        url: "/fileupload",
        processData: false, 
        // 파일 전송시 false, 기본은 true
        contentType: false, 
        // 파일 전송시 false, 기본은 true, json 전송시 "application/json; charset=utf-8"
        data : formData,
        async: false,
        // async를 끈다. 동기적으로 실행하게 됨.
        success : function (responce) {
            console.log('fileUploadFunc result')
            console.log(responce.result); 
        },
        error : function() {
            alert("파일 업로드 실패!");
        }
    });
}

// file check Function
function fileCheck(filename) {
    $.ajax({
        type: "POST",
        url: "/filecheck",
        data : {fileNameInput : filename},
        async: false,
        success : function (responce) {
            console.log(responce.result)
        },
        error : function() {
            alert("파일 체크 실패!")
        }
    })
}

// process active 
function active() {
    const fileUploadForm = document.querySelector(".fileUploadForm");
    const fileSourceTag = fileUploadForm.querySelector("input");
    const fileSource = fileSourceTag.files[0]
    const fileSourceName = fileSourceTag.files[0].name;
    
    // file upload and checking
    fileUploadFunc(fileSource, fileSourceName)
    fileCheck(fileSourceName)
    fileCheck(fileSourceName + '.xlsx')
}
