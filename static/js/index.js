import Dropzone from "dropzone"

import "dropzone/dist/dropzone.css";
import "../css/styles.css";

let myDropzone = new Dropzone("#upload-btn", {
    url: '/upload',
    uploadMultiple: false,
    maxFilesize: 10,
    thumbnailWidth: 250,
    thumbnailHeight: 250,
    maxFiles: 1,
    dictDefaultMessage: "",
    acceptedFiles: "image/jpeg,image/jpg,image/png",
    success: (file) => {
        getPredict(file.name)
    }
});

function getPredict(image) {
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'image': image
        })
    })
        .then(r => r.json())
        .then(response => {
            const obj = document.getElementById('object_name');

            if (response && response.message) {
                obj.innerText = response.message.name
            }else{
                obj.innerText = 'موردی یافت نشد'
            }
            obj.style.display = 'block'
        })
}
