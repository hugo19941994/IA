$(".uploadDocumentOnboarding").on("click", function (evt) {

var documentData = new FormData();
documentData.append('file', $('input#file.findDocumentOnboarding')[0].files[0]);
documentData.append('name', $('input#file.findDocumentOnboarding')[0].files[0].name);
$.ajax({
    url: "http://hugofs.com:8080/subir",
    type: 'POST',
    data: documentData,
    cache: false,
    contentType: false,
    processData: false,
    success: function (response) {
        alert("Document uploaded successfully.");
    }
});
});
