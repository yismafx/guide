const pptxgen = require("pptxgenjs");
const cheerio = require("cheerio");
const fs = require("fs").promises;

async function html2pptx(htmlFile, pptx) {
  const html = await fs.readFile(htmlFile, "utf-8");
  const $ = cheerio.load(html);

  const slide = pptx.addSlide();

  const bodyStyle = $("body").attr("style") || "";
  const bgMatch = bodyStyle.match(/background(?:-color)?:\s*([^;]+)/);
  const gradientMatch = bodyStyle.match(/background:\s*(linear-gradient[^;]+)/);

  if (gradientMatch) {
    slide.background = { color: "667eea" };
  } else if (bgMatch) {
    const bgColor = bgMatch[1].trim();
    if (bgColor.startsWith("#")) {
      slide.background = { color: bgColor.substring(1) };
    } else if (bgColor.startsWith("rgb")) {
      slide.background = { color: "FFFFFF" };
    } else {
      slide.background = { color: "FFFFFF" };
    }
  } else {
    slide.background = { color: "FFFFFF" };
  }

  $("h1").each((i, elem) => {
    const text = $(elem).text();
    const color = extractColor($(elem).css("color")) || "000000";
    slide.addText(text, {
      x: 0.5,
      y: 0.5 + i * 1.5,
      w: 9,
      h: 1,
      fontSize: 44,
      bold: true,
      color: color,
      align: "center"
    });
  });

  $("h2").each((i, elem) => {
    const text = $(elem).text();
    const color = extractColor($(elem).css("color")) || "000000";
    slide.addText(text, {
      x: 0.5,
      y: 1.5 + i * 1,
      w: 9,
      h: 0.8,
      fontSize: 32,
      color: color,
      align: "center"
    });
  });

  let yPos = 2.5;
  $("body > .content p, body > p, body > div > p").each((i, elem) => {
    const text = $(elem).text();
    if (text.trim()) {
      slide.addText(text, {
        x: 0.5,
        y: yPos,
        w: 9,
        h: 0.5,
        fontSize: 20,
        color: "333333"
      });
      yPos += 0.6;
    }
  });

  $("ul").each((i, elem) => {
    const items = [];
    $(elem).find("li").each((j, li) => {
      items.push({ text: $(li).text(), options: { bullet: true } });
    });

    if (items.length > 0) {
      slide.addText(items, {
        x: 1,
        y: yPos,
        w: 8,
        h: 4,
        fontSize: 20,
        color: "333333"
      });
    }
  });

  $(".author").each((i, elem) => {
    const text = $(elem).text();
    slide.addText(text, {
      x: 0.5,
      y: 6.5,
      w: 9,
      h: 0.5,
      fontSize: 18,
      color: "FFFFFF",
      align: "center"
    });
  });
}

function extractColor(colorStr) {
  if (!colorStr) return null;
  if (colorStr.startsWith("#")) return colorStr.substring(1);
  if (colorStr === "white") return "FFFFFF";
  if (colorStr === "black") return "000000";
  return null;
}

async function createPresentation() {
  console.log("Iniciando creacion de presentacion...");

  const pptx = new pptxgen();
  pptx.layout = "LAYOUT_16x9";
  pptx.author = "Yismary Quintero";
  pptx.title = "Trading Algoritmico Aumentado con IA Generativa - Modulo 0";
  pptx.subject = "Trading Algoritmico con IA";

  const slides = [
    "slide01.html",
    "slide02.html",
    "slide03.html",
    "slide04.html",
    "slide05.html",
    "slide06.html",
    "slide07.html",
    "slide08.html",
    "slide09.html",
    "slide10.html",
    "slide11.html",
    "slide12.html",
    "slide13.html",
    "slide14.html",
    "slide15.html",
    "slide16.html"
  ];

  for (let i = 0; i < slides.length; i++) {
    const slideNum = i + 1;
    const totalSlides = slides.length;
    console.log("Procesando " + slides[i] + " (" + slideNum + "/" + totalSlides + ")...");
    try {
      await html2pptx(slides[i], pptx);
      console.log("OK " + slides[i] + " completado");
    } catch (error) {
      console.error("ERROR procesando " + slides[i] + ":", error.message);
      throw error;
    }
  }

  const outputFile = "/mnt/user-data/outputs/Trading_Algoritmico_IA_Modulo0.pptx";
  console.log("\nGuardando presentacion en " + outputFile + "...");
  await pptx.writeFile({ fileName: outputFile });
  console.log("Presentacion creada exitosamente!");

  return outputFile;
}

createPresentation()
  .then(file => {
    console.log("\nEXITO: Presentacion guardada en " + file);
    process.exit(0);
  })
  .catch(error => {
    console.error("\nERROR:", error);
    process.exit(1);
  });
