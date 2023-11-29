const fs = require('fs');

// 读取CSV文件
fs.readFile('updated_data_new.csv', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    processData(data); // 处理CSV数据的函数
});

function processData(content) {
    const rows = content.split('\n'); // 按行分割
    const data = rows.map(row => row.split(',')); // 按逗号分割列数据

    let dict = {}
    for(let i = 0 ; i < data.length;i++){
        if(data[i][8]) data[i][8] = data[i][8].slice(0,-1)
        if(i === 0){
            data[i].push('co2_emission_range')
        }else{
            if(dict[data[i][0]]){
                data[i].push("")
            }else{
                dict[data[i][0]] = 1
                if(data[i][6] <= 500){
                    data[i].push("0-500(low)")
                } else if(500 < data[i][6] && 1000 > data[i][6]){
                    data[i].push("500-1000(moderate)")
                }else if(1000 < data[i][6] && 1500 > data[i][6]){
                    data[i].push("1000-1500(high)")
                }else{
                    data[i].push("1500+(very high)")
                }
            }
        }
    }

    const processedData = data.map(row => row.join(',')); // 将数据转换回CSV格式的行

    // 将处理后的CSV数据写入新文件
    fs.writeFile('processed_data_test.csv', processedData.join('\n'), 'utf8', (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log('CSV文件已导出');
    });
}

