const fs = require("fs");

// 读取CSV文件
fs.readFile("updated_data.csv", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  processData(data); // 处理CSV数据的函数
});

function processData(content) {
  const rows = content.split("\n"); // 按行分割
  const data = rows.map((row) => row.split(",")); // 按逗号分割列数据

  let dict = {};
  for (let i = 1; i < data.length; i++) {
    if(dict[data[i][0]]) {
        data[i][6] = ""
    } else {
        dict[data[i][0]] = 1
    }
  }

  const processedData = data.map((row) => row.join(",")); // 将数据转换回CSV格式的行

  // 将处理后的CSV数据写入新文件
  fs.writeFile("processed_data_test.csv", processedData.join("\n"), "utf8", (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log("CSV文件已导出");
  });
}
