// upload Function 
const fileUploadFunc = (fileSource, fileSourceName) => {
    // console.log(fileSource);
    // 파일을 보내기 위해서는 formData 안에 모든 정보를 담아서 보낸다.
    const fileDetails = JSON.stringify({
        name : fileSourceName
    })
    
    let formData = new FormData();
    formData.append('body', fileDetails)
    formData.append('file', fileSource);

    let result = false;

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
            let resultUploadTest = responce.result;
            console.log(resultUploadTest);
            if (!resultUploadTest.startsWith('INVALID') &&
                !resultUploadTest.startsWith('NOT EXIST FILE')) {
                result = true
            };
        },
        error : function() {
            alert("파일 업로드 실패!");
        }
    });
    return result;
}

// file check Function
const fileCheck = (filename) => {
    let result = false;
    $.ajax({
        type: "POST",
        url: "/filecheck",
        data : {fileNameInput : filename},
        async: false,
        success : function (responce) {
            result = responce.result
        },
        error : function() {
            alert("파일 체크 실패!")
        }
    })
    return result;
}

// process active 
const active = () => {
    const fileUploadForm = document.querySelector(".fileUploadForm");
    const fileSourceTag = fileUploadForm.querySelector("input");
    const fileSource = fileSourceTag.files[0]
    const fileSourceName = fileSourceTag.files[0].name;
    
    // file upload and checking
    if (fileUploadFunc(fileSource, fileSourceName)) {
        if (fileCheck(fileSourceName)) {
            console.log('uploading success!') // true

            if (fileCheck(fileSourceName + '.xlsx')) {
                console.log('checking xlsx success!')
            } else {
                console.log('checking xlsx fail!')
            }
        
        } else {
            console.log('checking txt fail!')
        }
    
    } else {
        console.log('uploading fail!')
    }
}
