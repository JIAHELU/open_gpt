const xlsx = require('xlsx');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

async function main() {
    const workbook = xlsx.readFile('D:\\CScience\\Git\\OpenGpt\\file.xlsx');
    const worksheet = workbook.Sheets[workbook.SheetNames[0]];

    const data = xlsx.utils.sheet_to_json(worksheet);

    const results = data.map((row) => {
        const {
            id,
            name,
            description,
            icon,
            demoInput,
            prompt,
            usedCount,
            embedding
        } = row;

        return {
            id,
            name,
            description,
            icon,
            demoInput,
            prompt,
            usedCount: Number(usedCount),
            embedding
        };
    });

    await prisma.openGptApp.createMany({
        data: results,
        skipDuplicates: true
    });

    console.log('XLSX 文件已成功写入数据库！');
}

main()
    .catch((error) => {
        console.error(error);
    })
    .finally(async () => {
        await prisma.$disconnect();
    });