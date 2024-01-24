from random import randrange

departements = [
    {"numero": "01", "nom": "ain", "prefecture": "bourg en bresse", "region": "auvergne rhône alpes"},
    {"numero": "02", "nom": "aisne","prefecture": "laon", "region": "hauts de france"},
    {"numero": "03", "nom": "allier","prefecture": "moulins", "region": "auvergne rhône alpes"},
    {"numero": "04", "nom": "alpes de haute provence",  "prefecture": "digne les bains", "region": "provence alpes côte d'azur"},
    {"numero": "05", "nom": "hautes alpes", "prefecture": "gap", "region": "provence alpes côte d'azur"},
    {"numero": "06", "nom": "alpes maritimes", "prefecture": "nice", "region": "provence alpes côte d'azur"},
    {"numero": "07", "nom": "ardèche", "prefecture": "privas", "region": "auvergne rhône alpes"},
    {"numero": "08", "nom": "ardennes", "prefecture": "charleville mézières", "region": "grand est"},
    {"numero": "09", "nom": "ariège", "prefecture": "foix", "region": "occitanie"},
    {"numero": "10", "nom": "aube", "prefecture": "troyes", "region": "grand est"},
    {"numero": "11", "nom": "aude", "prefecture": "carcassonne", "region": "occitanie"},
    {"numero": "12", "nom": "aveyron", "prefecture": "rodez", "region": "occitanie"},
    {"numero": "13", "nom": "bouches du rhône", "prefecture": "marseille", "region": "provence alpes côte d'azur"},
    {"numero": "14", "nom": "calvados", "prefecture": "caen", "region": "normandie"},
    {"numero": "15", "nom": "cantal", "prefecture": "aurillac", "region": "auvergne rhône alpes"},
    {"numero": "16", "nom": "charente", "prefecture": "angoulême", "region": "nouvelle aquitaine"},
    {"numero": "17", "nom": "charente maritime", "prefecture": "la rochelle", "region": "nouvelle aquitaine"},
    {"numero": "18", "nom": "cher", "prefecture": "bourges", "region": "centre val de loire"},
    {"numero": "19", "nom": "corrèze", "prefecture": "tulle", "region": "nouvelle aquitaine"},

    {"numero": "2A", "nom": "corse du sud", "prefecture": "ajaccio", "region": "corse"},
    {"numero": "2B", "nom": "haute corse", "prefecture": "tulle", "region": "corse"},

    {"numero": "21", "nom": "côte d'or", "prefecture": "dijon", "region": "bourgogne franche comté"},
    {"numero": "22", "nom": "côtes d'armor", "prefecture": "saint brieuc", "region": "bretagne"},
    {"numero": "23", "nom": "creuse", "prefecture": "guéret", "region": "nouvelle aquitaine"},
    {"numero": "24", "nom": "dordogne", "prefecture": "périgueux", "region": "nouvelle aquitaine"},
    {"numero": "25", "nom": "doubs", "prefecture": "besançon", "region": "bourgogne franche comté"},
    {"numero": "26", "nom": "drôme", "prefecture": "valence", "region": "auvergne rhône alpes"},
    {"numero": "27", "nom": "eure", "prefecture": "évreux", "region": "normandie"},
    {"numero": "28", "nom": "eure et loir", "prefecture": "chartres", "region": "centre val de loire"},
    {"numero": "29", "nom": "finistère", "prefecture": "quimper", "region": "bretagne"},
    {"numero": "30", "nom": "gard", "prefecture": "nîmes", "region": "occitanie"},
    {"numero": "31", "nom": "haute garonne", "prefecture": "toulouse", "region": "occitanie"},
    {"numero": "32", "nom": "gers", "prefecture": "auch", "region": "occitanie"},
    {"numero": "33", "nom": "gironde", "prefecture": "bordeaux", "region": "nouvelle aquitaine"},
    {"numero": "34", "nom": "hérault", "prefecture": "montpellier", "region": "occitanie"},
    {"numero": "35", "nom": "ille et vilaine", "prefecture": "rennes", "region": "bretagne"},
    {"numero": "36", "nom": "indre", "prefecture": "châteauroux", "region": "centre val de loire"},
    {"numero": "37", "nom": "indre et loire", "prefecture": "tours", "region": "centre val de loire"},
    {"numero": "38", "nom": "isère", "prefecture": "grenoble", "region": "auvergne rhône alpes"},
    {"numero": "39", "nom": "jura", "prefecture": "lons le saunier", "region": "bourgogne franche comté"},
    {"numero": "40", "nom": "landes", "prefecture": "mont de marsan", "region": "nouvelle aquitaine"},
    {"numero": "41", "nom": "loir et cher", "prefecture": "blois", "region": "centre val de loire"},
    {"numero": "42", "nom": "loire", "prefecture": "saint étienne", "region": "auvergne rhône alpes"},
    {"numero": "43", "nom": "haute loire", "prefecture": "le puy en velay", "region": "auvergne rhône alpes"},
    {"numero": "44", "nom": "loire atlantique", "prefecture": "nantes", "region": "pays de la loire"},
    {"numero": "45", "nom": "loiret", "prefecture": "orléans", "region": "centre val de loire"},
    {"numero": "46", "nom": "lot", "prefecture": "cahors", "region": "occitanie"},
    {"numero": "47", "nom": "lot et garonne", "prefecture": "agen", "region": "nouvelle aquitaine"},
    {"numero": "48", "nom": "lozère", "prefecture": "mende", "region": "occitanie"},
    {"numero": "49", "nom": "maine et loire", "prefecture": "angers", "region": "pays de la loire"},
    {"numero": "50", "nom": "manche", "prefecture": "saint lô", "region": "normandie"},
    {"numero": "51", "nom": "marne", "prefecture": "chalons en champagne", "region": "grand est"},
    {"numero": "52", "nom": "haute marne", "prefecture": "chaumont", "region": "grand est"},
    {"numero": "53", "nom": "mayenne", "prefecture": "laval", "region": "pays de la loire"},
    {"numero": "54", "nom": "meurthe et moselle", "prefecture": "nancy", "region": "grand est"},
    {"numero": "55", "nom": "meuse", "prefecture": "bar le duc", "region": "grand est"},
    {"numero": "56", "nom": "morbihan", "prefecture": "vannes", "region": "bretagne"},
    {"numero": "57", "nom": "moselle", "prefecture": "metz", "region": "grand est"},
    {"numero": "58", "nom": "nièvre", "prefecture": "nevers", "region": "bourgogne franche comté"},
    {"numero": "59", "nom": "nord", "prefecture": "lille", "region": "hauts de france"},
    {"numero": "60", "nom": "oise", "prefecture": "beauvais", "region": "hauts de france"},
    {"numero": "61", "nom": "orne", "prefecture": "alençon", "region": "normandie"},
    {"numero": "62", "nom": "pas de calais", "prefecture": "arras", "region": "hauts de france"},
    {"numero": "63", "nom": "puy de dôme", "prefecture": "clermont ferrand", "region": "auvergne rhône alpes"},
    {"numero": "64", "nom": "pyrénées atlantiques", "prefecture": "pau", "region": "nouvelle aquitaine"},
    {"numero": "65", "nom": "hautes pyrénées", "prefecture": "tarbes", "region": "occitanie"},
    {"numero": "66", "nom": "pyrénées orientales", "prefecture": "perpignan", "region": "occitanie"},
    {"numero": "67", "nom": "bas rhin", "prefecture": "strasbourg", "region": "grand est"},
    {"numero": "68", "nom": "haut rhin", "prefecture": "colmar", "region": "grand est"},
    {"numero": "69", "nom": "rhône", "prefecture": "lyon", "region": "auvergne rhône alpes"},
    {"numero": "70", "nom": "haute saône", "prefecture": "vesoul", "region": "bourgogne franche comté"},
    {"numero": "71", "nom": "saône et loire", "prefecture": "mâcon", "region": "bourgogne franche comté"},
    {"numero": "72", "nom": "sarthe", "prefecture": "le mans", "region": "pays de la loire"},
    {"numero": "73", "nom": "savoie", "prefecture": "chambéry", "region": "auvergne rhône alpes"},
    {"numero": "74", "nom": "haute savoie", "prefecture": "annecy", "region": "auvergne rhône alpes"},
    {"numero": "75", "nom": "paris", "prefecture": "paris", "region": "île de france"},
    {"numero": "76", "nom": "seine maritime", "prefecture": "rouen", "region": "normandie"},
    {"numero": "77", "nom": "seine et marne", "prefecture": "melun", "region": "île de france"},
    {"numero": "78", "nom": "yvelines", "prefecture": "versailles", "region": "île de france"},
    {"numero": "79", "nom": "deux sèvres", "prefecture": "niort", "region": "nouvelle aquitaine"},
    {"numero": "80", "nom": "somme", "prefecture": "amiens", "region": "hauts de france"},
    {"numero": "81", "nom": "tarn", "prefecture": "albi", "region": "occitanie"},
    {"numero": "82", "nom": "tarn et garonne", "prefecture": "montauban", "region": "occitanie"},
    {"numero": "83", "nom": "var", "prefecture": "toulon", "region": "provence alpes côte d'azur"},
    {"numero": "84", "nom": "vaucluse", "prefecture": "avignon", "region": "provence alpes côte d'azur"},
    {"numero": "85", "nom": "vendée", "prefecture": "la roche sur yon", "region": "pays de la loire"},
    {"numero": "86", "nom": "vienne", "prefecture": "poitiers", "region": "nouvelle aquitaine"},
    {"numero": "87", "nom": "haute vienne", "prefecture": "limoges", "region": "nouvelle aquitaine"},
    {"numero": "88", "nom": "vosges", "prefecture": "épinal", "region": "grand est"},
    {"numero": "89", "nom": "yonne", "prefecture": "auxerre", "region": "bourgogne franche comté"},
    {"numero": "90", "nom": "territoire de belfort", "prefecture": "belfort", "region": "bourgogne franche comté"},
    {"numero": "91", "nom": "essonne", "prefecture": "évry", "region": "île de france"},
    {"numero": "92", "nom": "hauts de seine", "prefecture": "nanterre", "region": "île de france"},
    {"numero": "93", "nom": "seine saint denis", "prefecture": "bobigny", "region": "île de france"},
    {"numero": "94", "nom": "val de marne", "prefecture": "créteil", "region": "île de france"},
    {"numero": "95", "nom": "val d'oise", "prefecture": "cergy pontoise", "region": "île de france"},
    ]

#########################################################################################
a=0             #intervalle
b=0             #intervalle
new=0           #nouveau nb         
last=0          #ancien nb 
d=""            #rep departement
r=""            #rep region
p=""            #rep prefecture

def BrepD(d):
    print('Bonne réponse')
    print('')
    print("Quelle est la préfecture de ",end='')
    return departements[last]["nom"]

def MrepD(d):
    print("FAUX !!!!!!!! Il s'agit de ",departements[last]["nom"])
    print('')
    print("Quelle est la préfecture de ",end='')
    return departements[last]["nom"]

def QP(p):
    if p == departements[last]["prefecture"]:
        print('Bonne réponse')
        print('')
        print("Quelle est la région où se trouve ",end='')
        return departements[last]["nom"]
    else :
        print("FAUX !!!!!!!! Il s'agit de ",departements[last]["prefecture"])
        print('')
        print("Quelle est la région où se trouve ",end='')
        return departements[last]["nom"]
    
def QR(r):
    if r == departements[last]["region"]:
        print('Bonne réponse')
        print('////////////////////////////////')
        print('')
        return ' '
    else :
        print("FAUX !!!!!!!! Il s'agit de ",departements[last]["region"])
        print('////////////////////////////////')
        print('')
        return ' '


#########################################################################################
#a=1
#b=15
#q=20
print("!!!Attention!!! tout doit être en minuscule avec des espaces, des apostrophes et des accents")
print("Sur quelle intervalle 'a' et 'b' veux-tu être interrogé")
# faire +1 apres le numero 20 à cause de la corse
while a<1 or a>95 :
    a = int(input('a: '))
    if a<1 or a>95 :
        print('réponse non valable') 
while b<a or b>96 :      
    b = int(input('b: '))
    if b<a or b>96:
        print('réponse non valable')

print("à combien de question souhaites-tu répondre")
q = int(input('Nombres de questions: '))

for i in range(q):
    new = randrange(a,b,1)     #département choisi aléatoirement dans l'intervalle donnée
    if new != last:
        last = new

        print('Quel est le département qui a pour numéro ',departements[last]["numero"])
        d = input('réponse : ')

        if d == departements[last]["nom"]:
            print(BrepD(d))
            p = input('réponse : ')
            print(QP(p))
            r = input('réponse : ')
            print(QR(r))

        else :
            print(MrepD(d))
            p = input('réponse : ')
            print(QP(p))
            r = input('réponse : ')
            print(QR(r))
