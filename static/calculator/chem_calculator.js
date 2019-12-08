
//用按钮代替原来的input file
$('#fileButton').click(function () {
        $('#fileChoose').click()
    });


//获取上传文件的文件名,并给文本框赋值
$('#fileChoose').change(function () {
    var filePath = this.value;
    var fileName = filePath.split('\\')[filePath.split('\\').length - 1];
    $('#filePathDisplay').val(fileName);
});


//将上传文件传递给后端
$('#upload').click(function ajax_response () {
    var formData = new FormData();
    var file = $('#fileChoose')[0].files[0];
    let result;
    formData.append('file', file);
    $.ajax
        ({
            url: "/calculator/upload_doc/",
            type: 'POST',
            processData: false,
            contentType: false,
            data:formData,
            async:false,
            success:function(response) {
                //后续处理
                result = response;
                t_column = response[0];
                data = response[1];

                var s = '';
                for(var i in data){
                    s += '<tr>';
                    for(var j in data[i]){
                        s += '<td>' + data[i][j] + '</td>';
                    }
                    s += '</tr>';
                }
                $('#tab').append(s);

                if(t_column===4){
                    $('#head1').css('display','table-header-group');
                }
                else if(t_column===5){
                    $('#head2').css('display','table-header-group');

                }
            }

        });
    return result;
});

