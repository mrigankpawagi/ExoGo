M.AutoInit();

for (var y = 0; y < 100; y++) {
    $("#planets").append("<button index=" + y + "></button>");
}

var planets;
var p;
var center = 0;

fetch("../db.json").then(function (res) {
    res.json().then(function (txt) {
        planets = txt;
        render();
        $("#loader").delay(100).fadeOut(400);
    });
})

function render() {
    center -= 250;
    $("#main").css("background-position", center + "px");
    p = getRandomSubarray(planets, 100);
    var btns = $("#planets button");
    for (var x = 0; x < 100; x++) {
        var w = 25 * (1 - 0.5 * Math.random());
        var m = 30 * (1 + Math.random());
        btns.eq(x).css({
            "width": w,
            "height": w,
            margin: m,
            left: 25 * (Math.random() * 2 - 1),
            top: 25 * (Math.random() * 2 - 1),
            "box-shadow": 'inset 0 0 0px 20px ' + getRandomColor() + ', 0 0 30px 1px white',
            "background-image": 'url(images/planets/' + (1 + x % 13) + '.png)'
        });
    }
}

$("#steer").click(render);


$("#planets button").click(function () {
    $("#chat").hide();
    $("#quiz").hide();
    $("#planets button").removeClass("active");
    $("#toggleQuiz i").text("quiz");
    $("#toggleChat i").text("try");
    $(this).addClass("active");
    $("#info").show();
    $("#planetName").text(p[$(this).attr("index")].PlanetIdentifier);
    $("#score p").eq(0).text(Math.round(100 - 100 * ((p[$(this).attr("index")].score - 13309) / 44019)) + "%");
    text = [p[$(this).attr("index")].PlanetIdentifier + " is a " + { "Confirmed planets": "confirmed", "Controversial": "cotroversial", "": "" }[p[$(this).attr("index")].ListsPlanetIsOn] + " plant that was discovered in " + p[$(this).attr("index")].DiscoveryYear + " by the " + p[$(this).attr("index")].DiscoveryMethod + " method.",
    "It is " + p[$(this).attr("index")].AgeGyr + " billion years old, and is located " + p[$(this).attr("index")].DistFromSunParsec + " parsecs away from our sun. Its radius is " + p[$(this).attr("index")].RadiusJpt + " times that of Jupyter, and its mass is " + p[$(this).attr("index")].PlanetaryMassJpt + " times that of Jupyter.",
    "It has a surface temperature of " + p[$(this).attr("index")].SurfaceTempK + " Kelvins, while its host star has a surface temperature of " + p[$(this).attr("index")].HostStarTempK + " Kelvins. The host star has a radius of " + p[$(this).attr("index")].HostStarRadiusSlrRad + " Solar Radii, and a mass of " + p[$(this).attr("index")].HostStarMassSlrMass + " Solar Masses. It is " + p[$(this).attr("index")].HostStarAgeGyr + " billion years old.",
    p[$(this).attr("index")].PlanetIdentifier + " takes " + p[$(this).attr("index")].PeriodDays + " days to complete one revolution around its host star.",
    "It " + ['has no known stellar binary companion.', 'a P-type binary (circumbinary).', 'an S-type binary.', 'is an orphan planet (without any star).'][p[$(this).attr("index")].TypeFlag]];
    $("#description").html(text.join("<br><br>"));
});
$("#closeInfo").click(function () {
    $("#info").hide();
    $("#planets button").removeClass("active");
});

$("#toggleChat").click(function () {
    $("#quiz").hide();
    $("#info").hide();
    $("#chat").toggle();
    $("#toggleQuiz i").text("quiz");
    $("#planets button").removeClass("active");
    if ($("#chat").css('display') == 'none')
        $("#toggleChat i").text("try");
    else
        $("#toggleChat i").text("close");
})
$("#toggleQuiz").click(function () {
    $("#chat").hide();
    $("#info").hide();
    $("#quiz").toggle();
    $("#planets button").removeClass("active");
    $("#toggleChat i").text("try");
    if ($("#quiz").css('display') == 'none')
        $("#toggleQuiz i").text("quiz");
    else
        $("#toggleQuiz i").text("close");
})

function getRandomSubarray(arr, size) {
    var shuffled = arr.slice(0), i = arr.length, temp, index;
    while (i--) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
    }
    return shuffled.slice(0, size);
} function getRandomColor() {
    var r = Math.round(55 + 200 * Math.random());
    var g = Math.round(55 + 200 * Math.random());
    var b = Math.round(55 + 200 * Math.random());
    return "rgba(" + r + "," + g + "," + b + ", 0.5)";
}
