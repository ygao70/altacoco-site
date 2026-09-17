import json
P = {"lookbook-01-wide":"OtXADkUh3-I","ec-sideboard":"UrQeWGobTnI","about-hero":"SRZcOAERBUQ","ec-lounge-chair":"7mmmEkyk0aQ",
"lookbook-01-detail-b":"ulh3-dLSXjI","post-sectional-2":"Gkig1kUYl4c","ec-sectional":"nQBc6clG3X4","lookbook-02-wide":"LKI3Dd146vI",
"post-sectional-1":"P0q_HK_-GGM","post-sectional-3":"RqO6kwm4tZY","ec-dining-table":"cXmER3VNxUA","lookbook-04-wide":"zGKRmwzplVc",
"ec-solid-wood-table":"yJ97mWnHTVE","ec-pendant":"KP7p0-DRGbg","lookbook-04-detail-b":"wby4nFO-m8o","lookbook-03-wide":"-_GU-VDIHnk",
"lookbook-03-detail-a":"kUd6KkVfbCY","lookbook-03-detail-b":"EKe_cbaqJ2A","ec-kids-bed":"iSO22I2l5uc","ec-wool-rug":"B2vrSzxm43U",
"ec-compact-sofa":"uNZpPRPEnY4","ec-floor-lamp":"faJf1aDiezQ","lookbook-01-detail-a":"H_eb_VfG2Ow","home-detail":"mGI8b4KFoFM",
"lookbook-02-detail-b":"TWOnvtstmeU","lookbook-02-detail-a":"8mNGNld9cBA","contact-studio":"DGRixfygKvE","about-scale":"pdCTX1harH4",
"about-location":"U-Dhokv9iXk","lookbook-04-detail-a":"JSUUbTs_UZ0","journal-sofa-depth":"_uOCL2SJMy4",
"home-outdoor":"whoL0IGd5Ec","lookbook-05-wide":"CrMr84Mb9Y4","lookbook-05-detail-a":"EE6_axVwfnM","lookbook-05-detail-b":"FPQIl8rU7Kk",
"ec-outdoor-sofa":"IA_qTLJK7ig","ec-outdoor-dining":"ARLPIlSHvXc"}
DESC = {
"lookbook-01-wide":("Home + Lookbook 01","白色沙发、木质圆茶几、绿植、挂画的客厅"),
"ec-sideboard":("Editor's Choice","木质边柜，上面有台灯和摆件"),
"about-hero":("About","窗边的扶手椅、脚凳和落地灯"),
"ec-lounge-chair":("Home + Editor's Choice","木地板上的浅色木框扶手椅"),
"lookbook-01-detail-b":("Lookbook 01","柜子上的雕塑感陶瓷台灯和书"),
"post-sectional-2":("Product post","米色羊羔绒沙发扶手特写"),
"ec-sectional":("Home + Editor's Choice","明亮客厅里的白色转角沙发和几何地毯"),
"lookbook-02-wide":("Lookbook 02","米色沙发 + 皮质脚凳的家庭客厅"),
"post-sectional-1":("Product post","灰色模块沙发、深色茶几"),
"post-sectional-3":("Product post","米色转角沙发、圆茶几、脚凳（横图，居中裁切）"),
"ec-dining-table":("Home + Editor's Choice","阳光下的小圆桌和木椅"),
"lookbook-04-wide":("Lookbook 04","木餐桌、黑色餐椅、吊灯、地毯"),
"ec-solid-wood-table":("Editor's Choice","窗边的浅色实木长餐桌"),
"ec-pendant":("Home + Editor's Choice","灰色圆顶吊灯"),
"lookbook-04-detail-b":("Lookbook 04","白色吊灯下的餐桌和软包椅"),
"lookbook-03-wide":("Home + Lookbook 03","木床头、白色床品、床头灯的卧室"),
"lookbook-03-detail-a":("Lookbook 03","床头柜、台灯和毛毯"),
"lookbook-03-detail-b":("Lookbook 03","华夫格抱枕和床品"),
"ec-kids-bed":("Editor's Choice","带帐篷顶的儿童木床房间"),
"ec-wool-rug":("Editor's Choice","黄麻地毯和皮沙发角落特写"),
"ec-compact-sofa":("Editor's Choice","焦糖色皮质小沙发和绿植"),
"ec-floor-lamp":("Editor's Choice","奶油色休闲椅和黄铜落地灯"),
"lookbook-01-detail-a":("Lookbook 01","木桌上的陶罐和书"),
"home-detail":("Home","阳光下的米色沙发 + 嵌套茶几 + 黄铜落地灯 + 绿植 + 挂画，一组家具的搭配"),
"lookbook-02-detail-b":("Lookbook 02","带藤篮和绿植的边柜"),
"lookbook-02-detail-a":("Lookbook 02","阳光下的羊羔绒圆凳"),
"contact-studio":("Contact","设计师手持材料样板的桌面"),
"about-scale":("About","手拿色卡、图纸的桌面"),
"about-location":("About","雾中的西北常青森林（横图）"),
"lookbook-04-detail-a":("Lookbook 04","简洁的木餐椅"),
"journal-sofa-depth":("Journal article","沙发座深侧面视角（横图）"),
"home-outdoor":("Home（Outdoor Design 板块）","黑色格栅凉棚下的灰色户外沙发、藤编边几、绿植"),
"lookbook-05-wide":("Lookbook 05","柚木户外沙发组配白色坐垫，热带植物背景"),
"lookbook-05-detail-a":("Lookbook 05","柚木框架和户外坐垫特写"),
"lookbook-05-detail-b":("Lookbook 05","露台上的白色铁艺小椅和绿植（横图，居中裁切）"),
"ec-outdoor-sofa":("Editor's Choice","地中海风格凉棚下的白色户外沙发"),
"ec-outdoor-dining":("Editor's Choice","小阳台上的折叠小餐桌和早餐"),
}
lines = ["#!/bin/bash", "# 把这个文件放在 site/images/ 里运行（或在 site/images 目录下运行）。", "# 从 Unsplash 官方下载接口下载每张图，宽度 2400px，自动用正确的文件名保存。", 'cd "$(dirname "$0")"', ""]
rows = []
for f, pid in P.items():
    page = f"https://unsplash.com/photos/{pid}"
    dl = f"https://unsplash.com/photos/{pid}/download?force=true&w=2400"
    lines.append(f'curl -L -sS "{dl}" -o "{f}.jpg" && echo "ok  {f}.jpg" || echo "FAIL {f}.jpg"')
    used, desc = DESC[f]
    rows.append(f"| `{f}.jpg` | {used} | {desc} | [页面]({page}) · [直接下载]({dl}) |")
lines.append('echo "done"')
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'images', 'download-photos.sh','w').write("\n".join(lines)+"\n")
md = """# 网站照片清单（Unsplash 精选）

所有图片来自 Unsplash，采用 [Unsplash License](https://unsplash.com/license)：可免费商用，无需署名（署名摄影师是礼貌但非必须）。
`home-hero.jpg` 已经是你自己提供的那张，不在此列。

## 最省事的方法

在终端运行（会自动下载全部 37 张并用正确文件名保存到 `site/images/`）：

```bash
cd ~/Documents/altacoco/site/images
bash download-photos.sh
```

## 手动下载

点"直接下载"会得到 2400px 宽的 JPG；把它改名成第一列的文件名，放进 `site/images/` 即可，刷新网页立刻生效。

| 保存为 | 用在哪 | 内容 | 链接 |
|---|---|---|---|
""" + "\n".join(rows) + "\n"
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'images', 'PHOTO-PICKS.md','w').write(md)
print(len(P))
