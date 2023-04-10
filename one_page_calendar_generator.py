import os, webbrowser, sys

def open_tag(tag):
    return "<"+tag+">"
def close_tag(tag):
    return "</" + tag + ">"
def check_leap(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 1
    return 0
def rotate(l, n):
    return l[n:] + l[:n]
def day(y):
    y -= 1
    return (2*(y//4-y//100+y//400)+(y-(y//4-y//100+y//400))+1)%7
def Render_Calendar(year):
    code = "<!DOCTYPE><html><head><title>"+str(year)+" Calendar</title><link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'><link href='https://fonts.googleapis.com/css?family=Graduate' rel='stylesheet'><link href='https://fonts.googleapis.com/css?family=Old Standard TT' rel='stylesheet'><style>table{height: 100%;width: 100%;}th{border: 5px solid #2b3f56;height: 7%;}tr{border: 2px solid #2f455f;height: 8%;}td{border: 1px solid #3f4f62;}th:hover{border: 10px solid #ffffff;background-color: #0f1826;cursor: pointer;transition: 0.25s;}tr:hover{border: 5px solid #cccccc;background-color: #0b1313;cursor: pointer;transition: 0.25s;}td:hover{border: 5px solid #aaaaaa;background-color: #404040;cursor: pointer;transition: 0.25s;}.yr{position: fixed;width: 98%;color: rgb(0, 255, 255);font-size: 50px;font-family: 'Graduate';font-weight: bold;text-align: center;}.dm{width: 8.4745762711864406779661016949153%;color: #cc6699;font-size: 25px;font-family: sans-serif;font-weight: normal;text-align: center;}.mts1{width: 13.075060532687651331719128329298%;color: #9966ff;font-size: 30px;font-family: monospace;font-weight: normal;text-align: center;}.mts2{width: 13.075060532687651331719128329298%;color: #cc33ff;font-size: 35px;font-family: monospace;font-weight: bold;text-align: center;}.mtsL{width: 13.075060532687651331719128329298%;color: #ff66ff;font-size: 25px;font-family: monospace;font-weight: normal;text-align: center;}.dts{width: 1.6949152542372881355932203389831%;color: rgb(133, 133, 133);font-size: 30px;font-family: 'Lato';font-weight: normal;text-align: center;}.lp{width: 1.6949152542372881355932203389831%;color: #ff66ff;font-size: 30px;font-family: 'Old Standard TT';font-weight: normal;text-align: center;}.sm{width: 1.6949152542372881355932203389831%;color: #9966ff;font-size: 30px;font-family: 'Lato';font-weight: normal;text-align: center;}.lm{width: 1.6949152542372881355932203389831%;color: #cc33ff;font-size: 30px;font-family: 'Lato';font-weight: bold;text-align: center;}.dys{width: 13.075060532687651331719128329298%;color: #ffff00;font-size: 30px;font-family: ;font-weight: normal;text-align: center;}.wkend{width: 13.075060532687651331719128329298%;color: #ff9900;font-size: 30px;font-family: 'Times New Roman', serif;font-weight: normal;text-align: center;}.sun{width: 13.075060532687651331719128329298%;color: #ff0000;font-size: 35px;font-family: Georgia, serif;font-weight: bold;text-align: center;}.yr:hover{width: 97.5%;font-size: 50px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.dm:hover{font-size: 25px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.mts1:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.mts2:hover{font-size: 40px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.mtsL{font-size: 30px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.dts:hover{font-size: 35pfont-weight: bolder;cursor: pointer;transition: 0.25s;}.lp:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.sm:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.lm:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.dys:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.wkend:hover{font-size: 35px;font-weight: bolder;cursor: pointer;transition: 0.25s;}.sun:hover{font-size: 40px;font-weight: bolder;cursor: pointer;transition: 0.25s;}</style></head><body bgcolor='#1b2536'>"
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    lm = ["January","March","May","July","August","October","December"]
    days = ["Sunday","Monday","Tuesday","Wednusday","Thursday","Friday","Saturday"]
    ordered_months = [["","",""],["","",""],["","",""],["","",""],["","",""],["","",""],["","",""]]
    leap, d = check_leap(year), day(year)
    for i in range(12):
        for j in range(3):
            if ordered_months[d][j] == "":
                ordered_months[d][j] = months[i]
                break
        if i in [0, 2, 4, 6, 7, 9, 11]:
            d = (d+3)%7
        elif i in [3, 5, 8, 10]:
            d = (d+2)%7
        else:
            d = (d+leap)%7
    code += open_tag("table")+open_tag("tr")+open_tag("th class=\"yr\"")+str(year)+close_tag("th")+close_tag("tr")+open_tag("tr")+open_tag("td colspan=5 rowspan=3 class=\"dm\"")+"Dates/Months"+close_tag("td")
    for i in range(3):
        if i != 0:
            code += open_tag("tr")
        for j in range(7):
            if ordered_months[j][i] in lm:
                code += open_tag("td class=\"mts2\"")+ordered_months[j][i]+close_tag("td")
            elif ordered_months[j][i] == "February":
                code += open_tag("td class=\"mtsL\"")+ordered_months[j][i]+close_tag("td")
            else:
                code += open_tag("td class=\"mts1\"")+ordered_months[j][i]+close_tag("td")
        code += close_tag("tr")
    for i in range(7):
        code += open_tag("tr")
        for j in range(5):
            n = (i+1)+(j*7)
            if n == 28+leap:
                code += open_tag("td class=\"lp\"")+str(n)+close_tag("td")
            elif n == 30:
                code += open_tag("td class=\"sm\"")+str(n)+close_tag("td")
            elif n == 31:
                code += open_tag("td class=\"lm\"")+str(n)+close_tag("td")
            elif n > 31:
                code += open_tag("td class=\"lm\"")+""+close_tag("td")
            else:
                code += open_tag("td class=\"dts\"")+str(n)+close_tag("td")
        for j in range(7):
            if days[j] == "Saturday":
                code += open_tag("td class=\"wkend\"")+days[j]+close_tag("td")
            elif days[j] == "Sunday":
                code += open_tag("td class=\"sun\"")+days[j]+close_tag("td")
            else:
                code += open_tag("td class=\"dys\"")+days[j]+close_tag("td")
        days = rotate(days, 1)
        code += close_tag("tr")
    code += close_tag("table")+close_tag("body")+close_tag("html")
    f = open(str(year)+"-Calendar.html", 'w')
    f.write(code)
    f.close()
    webbrowser.open(os.path.abspath(os.getcwd())+"\\"+str(year)+"-Calendar.html", new=2)

if __name__ == "__main__":
    Render_Calendar(int(sys.argv[1]))