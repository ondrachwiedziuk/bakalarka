---
documentclass: report
statement-kinds:
    definice:
        style: definition
        label: Definice
        counter: self
    tvrzeni:
        style: definition
        label: Tvrzení
        counter: self
    pozorovani:
        style: definition
        label: Pozorování
        counter: none
    priklad:
        style: definition
        label: Příklad
        counter: none
    lemma:
        style: definition
        label: Lemma
        counter: tvrzeni
    domnenka:
        style: definition
        label: Domněnka
        counter: tvrzeni
    dusledek:
        style: definition
        label: Důsledek
        counter: tvrzeni
    veta:
        style: definition
        label: Věta
        counter: tvrzeni
    fakt:
        style: definition
        label: Fakt
        counter: tvrzeni
    pozn:
        style: remark
        label: Poznámka
        counter: none
---
# Základní pojmy

Základním matematickým objektem, o\ kterém tato práce pojednává, je *uzel*. Obvykle se tímto pojmem myslí vnoření uzavřené jednoduché křivky do trojrozměrného prostoru. Ovšem tahle definice skýtá drobná úskalí v\ podobě takzvaných *divokých uzlů* (v angličtině *wild knots*), které jde jen velmi obtížně studovat. Např. následující uzel má jako svoji součást nekonečnou posloupnost zatočení. A takový v reálném světě nikdy nepotkáme.

![Divoký uzel](../img/wild_knot.pdf)

Abychom se těmto uzlům vyhnuli, budeme používat definici [@Murasugi, p. 6], využívající místo spojitých křivek pouze polygonální křivky. Tedy uzlem rozumíme jednoduchou uzavřenpu lomenou čáru. Takovýmto uzlům se pak říká *krotké uzly* (v angličtině *tame knots*). Množinu všech takových uzlů značíme $\mathcal{K}$.

![Trojlístek](../img/trefoil.pdf)

Příbuzným pojmem je *link*, což je konečné disjunktní sjednocení uzlů. Množinu všech linků značíme $\mathcal{L}$. Linky sdílejí s uzly mnoho vlastností, ovšem v\ této práci se jim budeme věnovat pouze v\ poslední kapitole.

Existuje nespočetně mnoho uzlů, a proto se nabízí otázka, jak je klasifikovat. Velmi přirozený způsob je zavést *ekvivalenci* uzlů. V reálném světě si můžeme uzly představit jako provázky, které mají slepené konce a jsou různě zamotány do prostoru. Tento provázek můžeme libovolně deformovat, ale nesmíme ho přetrhnout. Na základě toho pak můžeme dva uzly prohlásit za ekvivalentní, pokud dokážeme jeden získat z druhého pomocí takovýchto deformací. Tento způsob klasifikace je velmi intuitivní, tudíž by bylo vhodné ho reflektovat i v matematické teorii.

Pro uzel $K$ si nejprve zavedeme *základní pohyby* následovně:

TODO - přidat obrázek základních pohybů

1) Mějme hranu křivky $K$ danou vrcholy $A$ a $B$. Pak můžeme umístit nový vrchol $C$ na hranu $AB$. Naopak, pokud existuje vrchol $C$ na hraně $AB$, která náleží do uzlu $K$, můžeme ho odstranit.

2) Mějme hranu $AB$ v $K$ a nějaký vrchol $C$ ležící mimo $K$. Pak pokud platí, že $ABC \cap K = AB$, pak můžeme hranu $AB$ nahradit hranami $AC$ a $CB$. Inverzně můžeme za splnění obdobných podmínek nahradit hrany $AC$ a $CB$ za hranu $AB$.

Tyto dva pohyby reflektují intuitivní představu o tom, jak můžeme uzly deformovat. Následně můžeme definovat relaci ekvivalence tak, že uzly $K$ a $K'$ jsou ekvivalentní, pokud existuje konečná posloupnost základních pohybů, která transformuje jeden uzel v druhý. Tuto relaci značíme $K \cong K'$.

Jelikož je práce s objekty ve třech rozměrech velmi obtížná, zavedeme si *diagramy* uzlů. Jedná se o projekce uzlů do roviny, zatímco zachováváme informaci o kříženích tím, že spodní část křivky v místě křížení přerušíme. Zároveň zakážeme patologické případy, kdy dojde pouze k překryvu dvou částí křivky, který není křížením. Diagram uzlu $K$ budeme značit $D_K$. Množinu všech diagramů uzlu $K$ značíme $D(K)$.

Takto daný diagram se skládá z\ *oblouků*, jimiž rozumíme souvislé komponenty diagramu. Množinu všech oblouků diagramu $D_K$ značíme $O(D_K)$. Dále místa, kde dochází k\ přerušení křivky, nazýváme *křížení*. Toto křížení budeme zapisovat jako uspořádanou trojici oblouků, které se v daném místě kříží podle obrázku (TODO). Množinu všech křížení diagramu $D_K$ značíme $C(D_K)$.

Na diagramech můžeme definovat ekvivalenci. Dva diagramy $D_K$ a $D'_{K'}$ jsou ekvivalentní, pokud platí, že $K \cong K'$. Ovšem, můžeme ekvivalenci zavést přímo na diagramech a to pomocí tzv. *Reidemeisterových pohybů*. Jsou obdobou základních pohybů pro diagramy a platí, že dva diagramy jsou ekvivalentní, pokud jeden získáme z druhého pomocí konečné posloupnosti Reidemeisterových pohybů. Reidemeisterovy pohyby jsou znázorněny na obrázku \ref{rmobr}.

![Reidemeisterovy pohyby](../img/RM.pdf){#rmobr}

Na rozlišování uzlů budeme využívat *invarianty*. Invariantem $I$ rozumíme takové zobrazení z množiny všech uzlů do nějaké množiny, které je konstantní na ekvivalentních uzlech. Tedy pokud $K_1 \cong K_2$, pak $I(K_1) = I(K_2)$. Invariant se nazývá *úplný*, pokud platí, že $I(K_1) = I(K_2)$ implikuje $K_1 \cong K_2$. Jelikož je ekvivalence uzlů daná pomocí Reidemeisterových pohybů, stačí ověřit, že se invariant zachovává na těchto pohybech.

Mezi základní invarianty patří třeba *crossing number*, což je nejmenší možný počet křížení přes všechny diagramy jednoho uzlu. Dalšími příklady jsou *unknotting number*, *bridge number* nebo *genus*. V této práci se budeme věnovat invariantům založených na quandlovém barvení.

TODO - přidat orientované uzly
