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
    vetac:
        style: definition
        label: Věta
        counter: tvrzeni
    faktc:
        style: definition
        label: Fakt
        counter: tvrzeni
    lemmac:
        style: definition
        label: Lemma
        counter: tvrzeni
    domnenkac:
        style: definition
        label: Domněnka
        counter: tvrzeni
    tvrzenic:
        style: definition
        label: Tvrzení
        counter: tvrzeni
---
# Quandlové barvení uzlů

## Úvod do teorie uzlů

Základním matematickým objektem, o\ kterém tato práce pojednává, je *uzel*. Obvykle se tímto pojmem myslí vnoření uzavřené jednoduché křivky do trojrozměrného prostoru. Ovšem tahle definice skýtá drobná úskalí v\ podobě takzvaných *divokých uzlů* (v angličtině *wild knots*), které jde jen velmi obtížně studovat. Např. následující uzel má jako svoji součást nekonečnou posloupnost zatočení. A takový v reálném světě nikdy nepotkáme.

![Divoký uzel](../img/wild_knot.pdf)

Abychom se těmto uzlům vyhnuli, budeme používat definici [@Murasugi, p. 6], využívající místo spojitých křivek pouze polygonální křivky. Tedy uzlem rozumíme jednoduchou uzavřenou lomenou čáru. Takovýmto uzlům se pak říká *krotké uzly* (v angličtině *tame knots*). Množinu všech takových uzlů značíme $\mathcal{K}$.

![Trojlístek](../img/trefoil.pdf)

Příbuzným pojmem je *link*, což je konečné disjunktní sjednocení uzlů. Množinu všech linků značíme $\mathcal{L}$. Linky sdílejí s uzly mnoho vlastností, ovšem v\ této práci se jim budeme věnovat pouze v\ poslední kapitole. Jiným zobecněním je *orientovaný uzel*, kdy si na uzlu zvolíme orientaci. Pokud jde o link, orientace je dána na každém uzlu zvlášť.

Existuje nespočetně mnoho uzlů, a proto se nabízí otázka, jak je klasifikovat. Velmi přirozený způsob je zavést *ekvivalenci* uzlů. V reálném světě si můžeme uzly představit jako provázky, které mají slepené konce a jsou různě zamotány do prostoru. Tento provázek můžeme libovolně deformovat, ale nesmíme ho přetrhnout. Na základě toho pak můžeme dva uzly prohlásit za ekvivalentní, pokud dokážeme jeden získat z druhého pomocí takovýchto deformací. Tento způsob klasifikace je velmi intuitivní, tudíž by bylo vhodné ho reflektovat i v matematické teorii.

Pro uzel $K$ si nejprve zavedeme *základní pohyby* dle obrázku \ref{natural}:

![Základní pohyby](../img/natural.pdf){#natural}

1) Mějme hranu křivky $K$ danou vrcholy $A$ a $B$. Pak můžeme umístit nový vrchol $C$ na hranu $AB$. Naopak, pokud existuje vrchol $C$ na hraně $AB$, která náleží do uzlu $K$, můžeme ho odstranit.

2) Mějme hranu $AB$ v $K$ a nějaký vrchol $C$ ležící mimo $K$. Pak pokud platí, že $ABC \cap K = AB$, pak můžeme hranu $AB$ nahradit hranami $AC$ a $CB$. Inverzně můžeme za splnění obdobných podmínek nahradit hrany $AC$ a $CB$ za hranu $AB$.

Tyto dva pohyby reflektují intuitivní představu o tom, jak můžeme uzly deformovat. Následně můžeme definovat relaci ekvivalence tak, že uzly $K$ a $K'$ jsou ekvivalentní, pokud existuje konečná posloupnost základních pohybů, která transformuje jeden uzel v druhý. Tuto relaci značíme $K \cong K'$.

Jelikož je práce s objekty ve třech rozměrech velmi obtížná, zavedeme si *diagramy* uzlů. Jedná se o projekce uzlů do roviny, zatímco zachováváme informaci o kříženích tím, že spodní část křivky v místě křížení přerušíme. Zároveň zakážeme patologické případy, kdy dojde pouze k překryvu dvou částí křivky, který není křížením. Diagram uzlu $K$ budeme značit $D_K$. Množinu všech diagramů uzlu $K$ značíme $D(K)$.

Takto daný diagram se skládá z\ *oblouků*, jimiž rozumíme souvislé komponenty diagramu. Množinu všech oblouků diagramu $D_K$ značíme $O(D_K)$. Dále místa, kde dochází k\ přerušení křivky, nazýváme *křížení*. Toto křížení budeme zapisovat jako uspořádanou trojici oblouků, které se v daném místě kříží, ve tvaru $(a, b, c)$ podle obrázku \ref{crossing}. Množinu všech křížení diagramu $D_K$ značíme $C(D_K)$.

![Křížení](../img/crossing.pdf){#crossing}


Na diagramech můžeme definovat ekvivalenci. Dva diagramy $D_K$ a $D_{K'}$ jsou ekvivalentní, pokud platí, že $K \cong K'$. Navíc, můžeme ekvivalenci zavést přímo na diagramech a to pomocí tzv. *Reidemeisterových pohybů*. Jsou obdobou základních pohybů pro diagramy a platí, že dva diagramy jsou ekvivalentní, pokud jeden získáme z druhého pomocí konečné posloupnosti Reidemeisterových pohybů. Reidemeisterovy pohyby jsou znázorněny na obrázku \ref{rmobr}.

![Reidemeisterovy pohyby](../img/RM.pdf){#rmobr}

Na rozlišování uzlů budeme využívat *invarianty*. Invariantem $I$ rozumíme takové zobrazení z množiny všech uzlů do nějaké množiny, které je konstantní na ekvivalentních uzlech. Tedy pokud $K_1 \cong K_2$, pak $I(K_1) = I(K_2)$. Invariant se nazývá *úplný*, pokud platí, že $I(K_1) = I(K_2)$ implikuje $K_1 \cong K_2$. Jelikož je ekvivalence uzlů daná pomocí Reidemeisterových pohybů, stačí ověřit, že se invariant zachovává na těchto pohybech.

Mezi základní invarianty patří třeba *crossing number*, což je nejmenší možný počet křížení přes všechny diagramy jednoho uzlu. Dalšími příklady jsou *unknotting number*, *bridge number* nebo *genus*. V této práci se budeme věnovat invariantům založeným na quandlovém barvení.

## Úvod do teorie quandlů

Quandle vznikl jako algebraická struktura, která respektuje Reidemeisterovy pohyby, a je tak vhodná pro rozlišování uzlů. V této podkapitole rozvinu základní teorii kolem těchto algebraických struktur.

:::definice
*Quandlem* $Q = (C, *)$ rozumíme algebraickou strukturu nad množinou $C$ s binární operací $*$, splňující následující podmínky pro všechna $a, b, c \in C$:

1) $a * a = a$ (idempotence);

2) $\exists! x \in C: a * x = b$ (jednoznačné levé dělení, značíme $x = a *^{-1} b$);

3) $a*(b*c) = (a*b)*(a*c)$ (levá sebedistributivita).
:::

:::priklad
Příkladem quandle je například *triviální jednoprvkový quandle* $Q = (\{ a \}, *)$, kde $a * a = a$. Značme ho jako $T_1$. *Triviální quandle* nad $A$ definujeme tak, že vezmeme množinu $A$ a definujeme $a * b = b$ pro všechna $a, b \in A$. Takový quandle značíme $T_A$.
:::

:::priklad
Dalším příkladem může být quandle daný konjugací v grupě $G$. Pro $a, b \in G$ definujeme $a * b = a b a^{-1}$. Tento quandle značíme $\Conj{G}$.
:::

Na quandlech nyní zavedeme základní pojmy běžné i pro jiné algebraické struktury, jako homomorfismy, podalgebry a faktoralgebry běžné v univerzální algebře. Pomocí nich pak můžeme lépe porozumět vlastnostem quandlů.

:::definice
Mějme quandly $Q$ a $W$. Pak *quandlovým homomorfismem* $\varphi: Q \rightarrow W$ rozumíme zobrazení, které zachovává quandlovou operaci, tedy $\varphi(a * b) = \varphi(a) * \varphi(b)$ pro všechna $a, b \in Q$.
:::

:::definice
Mějme quandle $(Q, *)$. Pak *podquandlem* $W \preccurlyeq Q$ rozumíme dvojici $(W, *|_W)$, kde $W \subseteq Q$ a platí, že $W$ je uzavřená na operaci $*$ jakožto zúžení operace z $Q$.
:::

:::definice
Buď $Q$ quandle. Na něm zavedeme relaci ekvivalence $\alpha$ takovou, že $[a]_\alpha * [b]_\alpha = [a * b]_\alpha$ pro všechna $a, b \in Q$. Vzniklý quandle definovaný na blocích ekvivalence značíme $\faktor{Q}{\alpha}$ a nazýváme *faktorquandlem* quandlu $Q$ podle ekvivalence $\alpha$.
:::

Víme, že $a \mapsto [a]_\alpha$ je homomorfismus z $Q$ na $\faktor{Q}{\alpha}$. Také platí, že pokud máme homomorfismus $\varphi: Q \rightarrow W$, pak jádro, tj množina $\Ker \varphi = \{ (a, b) \in Q \times Q: \varphi(a) = \varphi(b) \}$, tvoří kongruenci na $Q$ a faktorquandle $\faktor{Q}{\Ker \varphi}$ je izomorfní s obrazem $\Ima \varphi(Q) \preccurlyeq W$. Jedná se o klasický výsledek univerzální algebry, který můžeme nalézt např. v knize [@Jezek2008]. Dalším takovým výsledkem je, že kongruence tvoří svaz:

Uvažujme kongruence $\alpha$ na quandlu $Q$ a na nich definujeme uspořádání inkluzí. Tato částečně uspořádaná množina tvoří svaz, který značíme $\Con{Q}$. Minimální prvek tohoto svazu značíme $0_Q$ a jedná se o kongruenci $\{ (a, a): a \in Q \}$. Maximální prvek značíme $1_Q$ a je roven $Q \times Q$.

## Quandlové barvení

Nyní definujeme pojmy *fundamentální quandle* a *quandlové barvení*, které nám dávají invarianty založené na quandlech.

:::definice
*Volným quandlem* $Q_X$ nad neprázdnou množinou $X$ rozumíme quandle takový, že pro zobrazení $f: X \rightarrow Q$, kde $Q$ je libovolný quandle, existuje právě jeden homomorfismus $\varphi: Q_X \rightarrow Q$ takový, že $\varphi(x) = f(x)$ pro všechna $x \in X$.
:::

Existence a jednoznačnost až na izomorfismus můžeme opět nalézt v knize [@Jezek2008].

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram, pak *fundamentálním quandlem* $Q_K$ rozumíme volný quandle nad množinou oblouků $O(D_K)$, který vyfaktorizujeme relací $\alpha$ definovanou následovně: pro každé křížení $(a, b, c) \in C(D_K)$ platí $a * b \alpha c$.
:::

:::tvrzenic
[@Joyce1982ACI].
Fundamentální quandle $Q_K$ je úplným invariantem až na orientaci.
:::

Fundamentální quandle dává sice velmi silný invariant, ale je těžké ho spočítat. Fundamentální quandle je nekonečný a určit, zda jsou dva takové quandly izomorfní, je velmi obtížné. Proto se spíše používá z něj odvozený invariant, kterému se říká *quandlové barvení*. Jedná se o počet homomorfismů z fundamentálního quandlu do námi zvoleného konečného quandlu. Jenže, můžeme si povšimnout, že vždy existuje triviální homomorfismus, který posílá všechny prvky z volného quandlu na jeden fixovaný prvek. Tudíž tyto homomorfismy zanedbáme. Tento invariant je sice slabší, ale lze mnohem snadněji spočítat.

:::definice
Mějme uzel $K$, jeho fundamentální quandle $Q_K$ a libovolný quandle $W$. Pak *počtem obarvení* $\Col{W}{K}$ rozumíme počet netriviálních homomorfismů $\varphi: Q_K \rightarrow W$. Tedy $\Col{W}{K} = |\Hom{Q_K}{W}| - |W|$.
:::

![Barvení pomocí quandlu](../img/coloring.pdf){#coloring}

Jak takový invariant funguje, si ukážeme na příkladu *Foxova quandlu*. Začneme definicí tohoto quandlu. Originálně je Foxovo barvení definováno jako barvení oblouků jednou ze tří barev tak, aby na každém křížení měly všechny tři oblouky buď stejnou barvu, nebo navzájem různou. Nyní vyjádříme Foxovo barvení pomocí jazyka quandlových homomorfismů. Foxův quandle $F$ definujeme následující tabulkou:

\begin{table}[h!]
\centering
\begin{tabular}{c|ccc}
$*$ & $1$ & $2$ & $3$ \\
\hline
$1$ & $1$ & $3$ & $2$ \\
$2$ & $3$ & $2$ & $1$ \\
$3$ & $2$ & $1$ & $3$
\end{tabular}
\end{table}

Nyní si vezměme uzel $K$ a jeho fundamentální quandle $Q_K$. Jelikož je fundamentální quandle definován jako volný quandle na obloucích diagramu modulo relace na kříženích, tak pokud každému oblouku přiřadíme jednu ze tří barev (tj. prvků z $F$), tak definujeme homomorfismus $f$ z $Q_K$ do $F$. Jenže ne každé obarvení je homomorfismus, protože musí splňovat relace dané kříženími. Mějme křížení $(a, b, c)$. Pak víme, že $f(a) * f(b) = f(c)$, viz obrázek \ref{coloring}. Tedy pokud $f(a) = f(b)$, pak i $f(c) = f(a)$. Naopak, pokud $f(a) \neq f(b)$, tak $f(c) \neq f(a), f(b)$. Toto nám dává přesně pravidla Foxova barvení.

<!-- Nyní si zvolme uzel $K$ a jeho fundamentální quandle $Q_K$. Pro každý oblouk $a \in O(D_K)$ si zvolme jeden z prvků $f(a) \in F$ tak, abychom dostali homomorfismus $f: Q_K \rightarrow F$. Jelikož je fundamentální quandle $Q_K$ definovaný na obloucích diagramu, tak každý homomorfismus lze vyjádřit tímto způsobem. Naopak ne pro každé přiřazení prvků $f(a)$ dostaneme homomorfismus. Pro náš případ si všimneme, že pro křížení $(a, b, c)$ platí, že když $f(a) = f(b)$, pak i $f(c) = f(a)$. Naopak, pokud $f(a) \neq f(b)$, tak $f(c) \neq f(a), f(b)$, což nám dává přesně pravidla Foxova barvení. -->

## Souvislost

V této sekci se budeme zabývat souvislými quandly. Tato třída je důležitá hned ze dvou důvodů. Prvním je, že všechny konečné quandly lze rozložit na souvislé podquandly. Druhým je, že fundamentální quandle uzlu je souvislý.

:::definice
Mějme quandle $Q$. Pak $L_q$ značí levou translaci o $q \in Q$, tedy $L_q(x) = q * x$. Grupa generovaná levými translacemi se značí $\Inn{Q}$ a nazývá se *grupa vnitřních automorfismů* quandlu $Q$.
:::

:::definice
Mějme quandle $Q$. Pokud platí, že je působení $\Inn{Q}$ na $Q$ tranzitivní, pak říkáme, že $Q$ je souvislý quandle.
:::

:::{.lemma #conn}
Mějme konečný quandle $Q$. Pak jsou následující tvrzení ekvivalentní:

1) $Q$ je souvislý;

2) pro každé dva prvky $a, b \in Q$ platí, že existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b,$$

kde $\varepsilon_i \in \{ -1, 1 \}$.
:::

:::proof
(1) $\Rightarrow$ (2): Mějme $a, b \in Q$. Jelikož je $Q$ konečný, tak platí, že $|\Inn{Q}| \leq |Q|!$, tedy $\Inn{Q}$ je konečná grupa. Tudíž pro každý prvek $\varphi \in \Inn{Q}$ existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že $\varphi = L_{x_1}^{\varepsilon_1} \circ L_{x_2}^{\varepsilon_2} \circ \dots \circ L_{x_n}^{\varepsilon_n}$, kde $L_x$ je levá translace o $x$. 

Jelikož $\Inn{Q}$ je tranzitivní, tak existuje $\varphi \in \Inn{Q}$ taková, že $\varphi(a) = b$. Tedy existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b.$$

(2) $\Rightarrow$ (1): Jelikož každé dva prvky dokážeme spojit konečnou posloupností translací, tak platí, že grupa $G$ daná levými translacemi $\Inn{Q}$ působí tranzitivně na $Q$. Tudíž je $Q$ souvislý.
:::

:::{.lemma #orbita}
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Pak platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle.
:::

:::proof
Zafixujme orbitu $W$. Pak platí, že $W$ je uzavřená na operaci $*$, jelikož pokud $a, b \in W$, tak $a * b = L_a(b) \in W$. Zároveň je uzavřená na levé dělení, jelikož pokud $a, b \in W$, tak $a *^{-1} b = L_a^{-1}(b) \in W$. Tedy $W$ je podquandle.
:::

:::priklad
Mezi souvislé quandly patří např. Foxův quandle $F$. Naopak, mezi nesouvislé patří triviální quandly $T_n$, kde $n > 1$. Tyto quandly se rozpadnou na $n$ jednoprvkových podquandlů $T_1$, které jsou triviálně souvislé.
:::

Obecně neplatí, že působením $\Inn{Q}$ na $Q$ dostaneme souvislé quandly. Je to z toho důvodu, že působení $\Inn{Q}$ na jednu orbitu $Q'$ může být tranzitivní, ale z pohledu té orbity se jedná o působení $\Aut{Q'}$. A tedy může nastat, že $\Inn{Q'}$ není tranzitivní na $Q'$. Pro konečné quandly však platí, že se dají rekurzivně rozložit na souvislé podquandly.

:::{.tvrzenic #rozklad}
[@ehrman2006toward].
Mějme quandle $Q$. Pak platí, že se dá jednoznačně rozložit na maximální souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$.
:::

:::proof
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Podle lemmatu \ref{orbita} platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle. Jelikož je $Q$ konečný, tak má konečně mnoho orbit. Pokud je orbita souvislá, tak jsme skončili. Pokud ne, znovu aplikujeme lemma \ref{orbita}. Takto pokračujeme, dokud nedostaneme rozklad na souvislé podquandly. Jelikož je $Q$ konečný a velikost orbit se zmenšuje, tak se vždy dostaneme do souvislého podquandlu.

Rozklad je jednoznačný, jelikož pokud by existovaly dva různé rozklady, tak by existovaly dva různé souvislé podquandly $W$ a $W'$, které se protínají, jenže by to znamenalo, že se dokážeme z každého prvku v $W$ dostat do $W'$ a naopak, což by znamenalo, že tvoří jeden souvislý quandle a jsou shodné, což je spor.
:::

:::definice
Mějme quandle $Q$. Pak *rozkladem* quandle $Q$ rozumíme rozklad na souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$. Podquandle $Q_i$ nazýváme *komponenta* $Q$.
:::

Nyní se podíváme, jak se chová souvislost při homomorfismech.

:::{.lemmac #hom}
[@bonatto2018structure].
Uvažujme quandly $Q$ a $W$, rozklad $Q$ jako ${Q_1, Q_2, \dots Q_n}$ a homomorfismus $\varphi: Q \rightarrow W$. Pak platí, že homomorfním obrazem $Q_i$ je souvislý podquandle $\varphi(Q_i) = W_i \preccurlyeq W$.
:::

:::proof
Mějme $a, b \in Q$ ve stejné komponentě. Pak podle lemmatu \ref{conn} existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že 

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b.$$

Nyní, když máme homomorfismus $\varphi: Q \rightarrow W$, tak platí, že

$$\varphi(x_1) *^{\varepsilon_1} (\varphi(x_2) *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (\varphi(x_n) *^{\varepsilon_n} \varphi(a)) \dots)) = \varphi(b).$$

Tedy platí, že $\varphi(a)$ a $\varphi(b)$ jsou ve stejné komponentě.
:::

Speciálně, pokud je $Q$ souvislý quandle, tak jeho homomorfním obrazem je také souvislý quandle.

:::{.lemmac #sofun}
[@Joyce1982ACI].
Mějme uzel $K$ a jeho fundamentální quandle $Q_K$. Pak platí, že $Q_K$ je souvislý quandle.
:::

:::proof
Mějme $a, b \in Q_K$ generátory. Pak chceme ověřit, že existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q_K$ taková, že $x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b$. Jenže, jelikož jsou $a, b$ generátory, tak odpovídají nějakým obloukům $a', b' \in O(D_K)$. Posloupnost prvků $x_1, x_2, \dots, x_n$ pak dostaneme tak, že začneme v $a'$ a půjdeme ve směru k $b'$. Pokaždé, když narazíme na křížení, kde je $x_i'$ most, tak si přidáme $x_i$ do posloupnosti s příslušným znaménkem operace. Jelikož $a, b$ leží na stejném uzlu, tak se tímto způsobem dostaneme z $a$ do $b$.

Tohle platí pro všechny generátory, tedy i pro všechny prvky $Q_K$, jelikož každý prvek je generován posloupností generátorů. Tudíž je $Q_K$ souvislý quandle.
:::

Z lemmat \ref{hom} a \ref{sofun} plyne, že obraz fundamentálního quandlu je souvislý quandle. Jenže to znamená, že nám při výpočtu $\Col{Q}{K}$ stačí uvažovat pouze souvislé quandly. Speciálně je jedním z důsledků následující lemma:

:::{.lemma #suma}
Mějme quandle $Q$, který není souvislý, a uzel $K$. Pak platí, že

$$\Col{Q}{K} = \sum_{i=1}^n |\text{Col}_{Q_i}(K)|,$$

kde $Q_i$ jsou komponenty rozkladu $Q$.
:::

:::proof
Mějme homomorfismus $\varphi \in \text{Hom}(Q_K, Q)$. Jelikož je $Q_K$ podle \ref{sofun} souvislý, tak podle lemmatu \ref{hom} platí, že $\varphi(Q_K)$ je souvislý podquandle $Q$. Jelikož se $Q$ rozkládá na komponenty, které jsou souvislé, tak platí, že $\varphi$ náleží do $\text{Hom}(Q_K, Q_i)$ pro nějaké $i$. Zároveň patří nejvýše do jedné takové množiny, jelikož jsou orbity disjunktní. Jelikož je $\varphi$ libovolný homomorfismus, tak platí, že

$$\Col{Q}{K} = \sum_{i=1}^n |\text{Col}_{Q_i}(K)|.$$
:::

