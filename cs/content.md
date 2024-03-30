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

Intuitivně je poměrně jasné, co by uzel měl být. Tedy vnoření uzavřené křivky do trojrozměrného prostoru. Ovšem tahle definice skýtá drobná úskalí v\ podobě takzvaných *divokých uzlů* (v angličtině *wild knots*), které jde jen velmi obtížně studovat. Např. následující uzel má jako svoji součást nekonečnou posloupnost zatočení. A takový v reálném světě nikdy nepotkáme.

![Divoký uzel](../img/wild_knot.pdf)

Abychom se těmto uzlům vyhnuli, budeme používat definici [@Murasugi, p. 6], využívající místo spojitých křivek polygonální křivky. Takovýmto uzlům se pak říká *krotké uzly* (v angličtině *tame knots*).

:::definice
*Uzlem* rozumíme lomenou uzavřenou jednoduchou křivku $K$ vnořenou do prostoru $\R^3$. Množinu všech takových uzlů značíme $\mathcal{K}$.
:::

![Trojlístek](../img/trefoil.pdf)

Nyní bychom na těchto křivkách zavedli, co znamená, že jsou uzly ekvivalentní. Intuitivně, jeden dokážeme "přemotat" v druhý. Formálně budeme působit konečnou posloupností deformací působících na jeden z nich, abychom dostali ten druhý.

Pro uzel $K$ definujme *základní pohyby* následovně:

1) Mějme hranu křivky $K$ danou vrcholy $A$ a $B$. Pak můžeme umístit vrchol $C$ na hranu $AB$. Inverzně můžeme tento vrchol $C$ smazat.

2) Mějme hranu $AB$ v $K$ a nějaký vrchol $C$ ležící mimo $K$. Pak pokud $ABC \cap K = AB$, pak můžeme hranu $AB$ nahradit hranami $AC$ a $CB$. Inverzně můžeme za splnění obdobných podmínek nahradit $AC$ a $CB$ za $AB$.

Pokud máme uzly $K$ a $K'$ takové, že existuje konečná posloupnost základních pohybů transformující jeden v druhý, pak říkáme, že jsou $K$ a $K'$ *ekvivalentní*. Značíme $K \cong K'$.

Abychom se nám s uzly lépe pracovalo, zavedeme projekci uzlu do roviny.

Pro uzel $K$ definujeme *diagram* $D_K$, který je projekcí $K$ do $\R^2$ takovou, že je prostá až na konečně mnoho bodů, nazýváme je *křížení*, pro které ovšem platí, že jsou obrazem právě dvou bodů z $K$ a ty nejsou pouze body dotyku, ale křížení v intuitivním smyslu. Křížení jsou znázorněna tak, že spodní část křivky je v místě křížení přerušená. Množinu všech příslušných diagramů uzlu rozumíme $D(K)$. Obloukem rozumíme souvislé komponenty diagramu. Množinu oblouků daného diagramu $D_K$ budeme značit $O(D_K)$. Množinu všech křížení, reprezentovanou uspořádanou trojicí příslušných oblouků, budeme značit $C(D_K)$. 

Diagram není určen jednoznačně ani pro konkrétní uzel $K$, natož pro jeho ekvivalenty. Avšak lze zavést obdobu základních pohybů pro diagramy.

Mějme uzel $K$ a jeho diagram $D_K$. Pak pro ně definujeme Reidemeisterovy pohyby vyjádřené obrázkem \ref{rmobr}:

![Reidemeisterovy pohyby](../img/RM.pdf){#rmobr}


:::{.fakt #rm}
Uzly $K_1$ a $K_2$ jsou ekvivalentní, právě tehdy když jsou jejich diagramy $D_1$ a $D_2$ ekvivalentní pomocí Reidemeisterových pohybů.
:::

Klasická výpočetní otázka zní, jestliže dostaneme dva zadané libovolné uzly, dokážeme o nich říct, zda jsou ekvivalentní? Metodou, jak ukázat, že uzly nejsou ekvivalentní, je pomocí invariantů.

:::definice
Mějme množinu všech uzlů $\mathcal{K}$ a libovolnou množinu $A$. Pak *invariantem* rozumíme takové zobrazení $I: \mathcal{K} \rightarrow A$, že pokud $K_1 \cong K_2$, pak $I(K_1) = I(K_2)$ pro všechny takové uzly $K_1, K_2 \in \mathcal{K}$. Říkáme, že $I$ je *úplný invariant*, pokud platí, že $I(K_1) = I(K_2)$ implikuje $K_1 \cong K_2$.
:::

Z faktu @rm plyne, že nám stačí ověřit, zda se invariant zachovává na Reidemeistrovy pohyby.

Nyní si uvedeme několik příkladů invariantů, které budeme využívat v následujících kapitolách.

<!-- :::definice
Buď $K$ uzel. Pak *počtem křížení* $c(K)$ (anglicky *crossing number*) rozumíme $c(K) = \min_{D \in D(K)} c(D)$, kde $c(D)$ je počet křížení v daném diagramu.
:::

:::pozorovani
Počet křížení $c(K)$ je invariant.
:::

:::definice
Buď $K$ uzel. Pak *rozvazujícím číslem* $u(K)$ (anglicky *unknot number*) rozumíme číslo takové, že je rovno minimálnímu počtu Reidemeistrových pohybů 1 až 3 potřebných k dosažení rozvázání uzlu.
::: -->

## Copánky

Jedním z užitečných pohledů na uzly je přes takzvané copánky. Něco o historii.

:::definice
Buď zadané číslo $n$. Pak $B_n$ značí grupu danou prezentací $B_n = \langle \sigma_1, \sigma_2, \dots, \sigma_{n-1} |\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}; \sigma_i \sigma_j = \sigma_j \sigma_i \rangle$, kde $i, j \in \{ 1, 2, \dots, n - 1 \}; |i - j| \geq 2$.
:::

Copánky si můžeme představit jako $n$ šňůrek natažených mezi dvěma deskami, přičemž pro ně platí Reidemeisterovy pohyby 2 a 3. Skládání $a \cdot b$ funguje tak, že se vezme spodní deska z $a$ a přilepí se k horní desce $b$ tak, aby na sebe navazovaly provázky, a pak se ty desky odstraní, aby byly opět jenom horní a dolní. Prvky $b$ tedy budeme ztotožňovat s příslušnou geometrickou konstrukcí. 

![Příklad copánku](../img/braid.pdf)

<!--
:::lemma
Mějme copánkovou grupu $B_n$ a symetrickou grupu $S_n$. Pak existuje kanonická projekce $\pi_n : B_n \twoheadrightarrow S_n$ definovaná vztahy, na generátorech $B_n$ následovně: $\forall i \in \{ 1, 2, \dots, n - 1 \}: \sigma_i^2 = 1$.
:::

Neformálně řečeno, pokud máme copánek a očíslujeme si dané šňůrky na jednom konci, tak na tom druhém dostaneme permutaci těchto čísel. Kanonická projekce pak tedy posílá copánky na příslušné permutace.
-->

Mějme copánkovou grupu $B_n$ . Pak *uzávěrem* $b \in B_n$ rozumíme uzel $K_b$ takový, který vznikne z $b$ tak, že konce šňůrek přilepíme k sobě tak, že $i$-tá šňůrka zhora se přilepí k $i$-té šňůrce zdola. Tímto způsobem nevznikne vždy uzel podle naší definice, ale obecně vznikne *link*, což je disjunktní sjednocení konečně mnoha uzlů.

![Lepení copánku](../img/glue.pdf)

:::veta
(Alexanderova věta).
Pro každý uzel $K$ existuje číslo $n \in \N$ a $b \in B_n$, že $K$ je ekvivalentní uzávěru $K_b$.
:::

:::definice
Pro daný uzel $K$ rozumíme *copánkovým indexem* $s(K)$ (anglicky *braid index*) nejmenší číslo $n$ takové, že existuje $b \in B_n$ tak, že $K$ je ekvivalentní uzávěru $K_b$.
:::

:::pozorovani
Copánkové číslo $s(K)$ je invariant.
:::

## Quandly

Mezi další invarianty může patřit počet barvení uzlu algebraickou strukturou $Q$ pomocí pravidel odvozených ze zachovávání Reidemeisterových pohybů.

:::definice
*Quandlem* $Q = (C, *)$ rozumíme algebraickou strukturu nad (konečnou) množinou $A$ s binární operací $*$, splňující následující podmínky pro všechna $a, b, c \in C$:

1) $a * a = a$ (idempotence);

2) Existuje právě jedno $x \in C$ splňující $a * x = b$ ;(jednoznačné levé dělení), budeme značit $x = a *^{-1} b$;

3) $a*(b*c) = (a*b)*(a*c)$ (levá samodistributivita).
:::

Barvení uzlu $K$ funguje následujícím způsobem. Nejprve si zvolíme orientaci křivky $K$. Pak každému oblouku $a$ diagramu $D_K$ přiřadíme nějaký prvek $f(a) \in C$ tak, že když procházíme uzel v námi zvoleném směru, tak pokaždé, když narazíme na konec oblouku $a$, tak hodnota navazujícího oblouku $c$ je rovna $f(c) = f(b) * f(a)$, kde $b$ je most v daném křížení. Příslušnou funkci $f$ nazýváme *obarvením* uzlu $K$ quandlem $Q$. Velikost množiny všech takových obarvení pak značíme $\Col{Q}{K}$ a jedná se o invariant. Formálně si barvení zavedeme pomocí fundamentálního quandlu.

![Barvení pomocí quandlu](../img/coloring.pdf)

:::definice
Mějme quandly $Q$ a $W$. Pak *homomorfismem* $\varphi: Q \rightarrow W$ rozumíme zobrazení, které zachovává quandlovou operaci, tedy $\varphi(a * b) = \varphi(a) * \varphi(b)$ pro všechna $a, b \in Q$.
:::

:::definice
Mějme quandle $(Q, *)$. Pak *podquandlem* $W$ rozumíme dvojici $(W, *|_W)$ podmnožinu $W \subseteq Q$ takovou, že je uzavřená na operaci $*$ jakožto operaci z $Q$. Vztah značíme $W \preccurlyeq Q$.
:::

:::definice
Buď $Q$ quandle. Na něm zavedeme relaci ekvivalence $\alpha$ takovou, že $[a]_\alpha * [b]_\alpha = [a * b]_\alpha$ pro všechna $a, b \in Q$. Takový quandle značíme $Q/\alpha$ a nazýváme *faktorquandlem*.
:::

Také platí, že $a \mapsto [a]_\alpha$ je homomorfismus z $Q$ na $Q/\alpha$. Také platí, že (citace) pokud máme homomorfismus $\varphi: Q \rightarrow W$, jádro, tj množina $\Ker \varphi = \{ (a, b) \in Q \times Q: \varphi(a) = \varphi(b) \}$, tvoří kongruenci na $Q$ a faktorquandlem $Q/\Ker \varphi$ je izomorfní s obrazem $\Ima \varphi(Q) \preccurlyeq W$.

:::definice
*Volným quandlem* $Q_X$ nad neprázdnou množinou $X$ rozumíme quandle takový, že pokud máme zobrazení $f: X \rightarrow Q$, kde $Q$ je libovolný quandle, tak existuje právě jeden homomorfismus $\varphi: Q_X \rightarrow Q$ takový, že $\varphi(x) = f(x)$ pro všechna $x \in X$.
:::

<!--

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram. Pak *obarvením* $f: Q \rightarrow O(D_K)$ rozumíme funkci takovou, že každému oblouku $a \in O(D_K)$ přiřadí prvek z $C$ takový, že splňuje $f(b) * f(a) = f(c)$ pro všechny oblouky $a,b,c \in O(D_K)$ takové, že $(a, b, c) \in C(D_K)$. Velikost množiny všech takových obarvení pak značíme $\Col{Q}{K}$.
:::


:::tvrzeni
Barvení $\Col{Q}{K}$ je invariant.
:::

Otázka zní, jakým quandlem barvit? Můžeme si nějaký pevně zvolit, ovšem můžeme se trefit do takového, že existují jenom triviální barvení. Nebo si můžeme říct, že si sestavíme quandl podle relací daných kříženími.

-->

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram, pak *fundamentálním quandlem* $Q_K$ rozumíme volný quandle nad množinou oblouků $O(D_K)$ modulo relace dané kříženími $C(D_K)$ takové, že pro každé křížení $(a, b, c) \in C(D_K)$ platí $a * b = c$.
:::

:::tvrzeni
[@Joyce1982ACI].
Fundamentální quandl $Q_K$ je úplným invariantem.
:::

:::definice
Mějme uzel $K$, jeho fundamentální quandle $Q_K$ a libovolný quandle $W$. Pak *počtem obarvení* $\Col{W}{K}$ rozumíme počet homomorfismů $\varphi: Q_K \rightarrow W$. Tedy $\Col{W}{K} = |\Hom{Q_K}{W}|$.
:::

:::pozorovani
Počet obarvení $\Col{W}{K}$ je invariant.
:::

## Invarianty konečného typu

Něco o Vassilievových invariantech. Tato kapitola je jen nástřel.

:::definice
*Singulárním* uzlem $K^\bullet$ s $n$ protnutími rozumíme uzel takový, že sám sebe protíná v $n$ bodech právě dvěma úseky.
:::

![Singulární uzel s 1 křížením](../img/singular.pdf)

:::definice
Mějme singulární uzel $K^{\bullet}$ s $n \geq 1$ a invariant $v$, zvolíme si nějaké protnutí. Pak pro dané protnutí *Vassilievovou skein relací* nazýváme rovnici:

$$v(K^{\bullet}) = v(K^+) - v(K^-)$$,

kde $K^{\bullet}$, $K^+$ a $K^-$ odpovídají obrázku \ref{skein}.
:::

![Vassilievova skein relace](../img/skein.pdf){#skein}

:::definice
Invariant $v$ se nazývá *Vassilievův*, nebo také *konečného typu* stupně $\leq m$, pokud platí, že pro každý singulární uzel $K^\bullet$ s počtem protnutí $> m$ platí $v(K^\bullet) = 0$. Řekneme, že je stupně $m$, pokud je stupně $\leq m$, ale není stupně $\leq m-1$.
:::

:::tvrzeni
Vzorec pro Vassilievův invariant.
:::

# Triviální barvení

V této kapitole se budeme zabývat charakterizací quandlů, které mají pouze triviální barvení.

## Souvislost

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

(2) $\Rightarrow$ (1): Jelikož každé dva prvky dokážeme spojit konečnou posloupností prvků, tak platí, že grupa $G$ daná levými translacemi $\Inn{Q}$ působí tranzitivně na $Q$. Tudíž je $Q$ souvislý.
:::

:::{.lemma #orbita}
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Pak platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle.
:::

:::proof
Zafixujme si orbitu nějakou $W$. Tak platí, že $W$ je uzavřená na operaci $*$, jelikož pokud $a, b \in W$, tak $a * b = L_a(b) \in W$. Zároveň je uzavřená na levé dělení, jelikož pokud $a, b \in W$, tak $a *^{-1} b = L_a^{-1}(b) \in W$. Tedy $W$ je podquandle.
:::

:::{.tvrzeni #rozklad}
[@ehrman2006toward].
Mějme quandle $Q$. Pak platí, že se dá jednoznačně rozložit na maximální souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$.
:::

:::proof
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Podle lemmatu @orbita platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle. Jelikož je $Q$ konečný, tak má konečně mnoho orbit. Pokud je orbita souvislá, tak jsme skončili. Pokud ne, znovu aplikujeme lemma @orbita. Takto pokračujeme, dokud nedostaneme rozklad na souvislé podquandly. Jelikož je $Q$ konečný a velikost orbit se zmenšuje, tak se vždy dostaneme do souvislého podquandlu.

Rozklad je jednoznačný, jelikož pokud by existovaly dva různé rozklady, tak by existovaly dva různé souvislé podquandly $W$ a $W'$, které se protínají, jenže by to znamenalo, že se dokážeme z každého prvku v $W$ dostat do $W'$ a naopak, což by znamenalo, že tvoří jeden souvislý quandle a jsou shodné, což je spor.
:::

:::definice
Mějme quandle $Q$. Pak *rozkladem* quandle $Q$ rozumíme rozklad na souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$. Subquandle $Q_i$ nazýváme *komponenta* $Q$.
:::

:::{.lemma #hom}
[@bonatto2018structure].
Uvažujme quandly $Q$ a $W$, rozklad $Q$ jako ${Q_1, Q_2, \dots Q_n}$ a homomorfismus $\varphi: Q \rightarrow W$. Pak platí, že homomorfním obrazem $Q_i$ je souvislý podquandle $\varphi(Q_i) = W_i \preccurlyeq W$.
:::

:::proof
Mějme $a, b \in Q$ ve stejné komponentě. Pak podle lemmatu @conn existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že 

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b.$$

Nyní, když máme homomorfismus $\varphi: Q \rightarrow W$, tak platí, že

$$\varphi(x_1) *^{\varepsilon_1} (\varphi(x_2) *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (\varphi(x_n) *^{\varepsilon_n} \varphi(a)) \dots) = \varphi(b).$$

Tedy platí, že $\varphi(a)$ a $\varphi(b)$ jsou ve stejné komponentě.
:::

Speciálně, pokud je $Q$ souvislý quandle, tak jeho homomorfním obrazem je také souvislý quandle.

:::{.lemma #sofun}
[@Joyce1982ACI].
Mějme uzel $K$ a jeho fundamentální quandle $Q_K$. Pak platí, že $Q_K$ je souvislý quandle.
:::

:::proof
Mějme $a, b \in Q_K$ generátory. Pak chceme ověřit, že existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q_K$ taková, že $x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b$. Jenže, jelikož jsou $a, b$ generátory, tak odpovídají nějakým obloukům $a', b' \in O(D_K)$. Posloupnost prvků $x_1, x_2, \dots, x_n$ pak dostaneme tak, že začneme v $a'$ a budeme ve směru k $b'$. Pokaždé, když narazíme na křížení, kde je $x_i'$ most, tak si přidáme $x_i$ do posloupnosti s příslušným znaménkem operace. Jelikož $a, b$ leží na stejném uzlu, tak se tímto způsobem dostaneme z $a$ do $b$.

Tohle platí pro všechny generátory, tedy i pro všechny prvky $Q_K$, jelikož každý prvek je generován posloupností generátorů. Tudíž je $Q_K$ souvislý quandle.
:::

:::{.lemma #suma}
Mějme quandle $Q$, který není souvislý, a uzel $K$. Pak platí, že

$$\Col{Q}{K} = \sum_{i=1}^n |\text{Col}_{Q_i}(K)|,$$

kde $Q_i$ jsou komponenty rozkladu $Q$.
:::

:::proof
Mějme homomorfismus $\varphi \in \text{Hom}(Q_K, Q)$. Jelikož je $Q_K$ podle @sofun souvislý, tak podle lemmatu @hom platí, že $\varphi(Q_K)$ je souvislý podquandle $Q$. Jelikož se $Q$ rozkládá na komponenty, které jsou souvislé, tak platí, že $\varphi$ náleží do $\text{Hom}(Q_K, Q_i)$ pro nějaké $i$. Zároveň patří nejvýše do jedné takové množiny, jelikož jsou orbity disjunktní. Jelikož je $\varphi$ libovolný, tak platí, že

$$\Col{Q}{K} = \sum_{i=1}^n |\text{Col}_{Q_i}(K)|.$$
:::

## Reduktivita

Tohle bude velmi výživná kapitolka.

:::definice
Buď $n \in \N$. Pak quandle $Q$ nazýváme *$n$-reduktivní*, pokud platí, že všechny $a, b, c_1, c_2, \dots, c_n \in Q$ splňují:

$$((\dots(a * c_1) \dots) * c_{n-1}) * c_n = ((\dots(b * c_1)\dots) * c_{n-1}) * c_n$$.

Říkáme, že $Q$ je *reduktivní*, pokud existuje $n \in \N$, že je $n$-reduktivní.
:::

:::definice
Lokální reduktivnost
:::

:::{.lemma #pumping}
Pokud všechny orbity jsou lokálně reduktivní, tak je quandle lokálně reduktivní.
:::

:::{.lemma #local}
Pro konečné quandly platí, že je lokálně reduktivní, právě tehdy když je reduktivní.
:::

:::{.lemma #redsou}
Jediný souvislý reduktivní quandle je triviální quandle velikosti $1$.
:::

:::tvrzeni
Buď $Q$ quandle. Pak jsou následující podmínky ekvivalentní:

1) $Q$ je reduktivní.

2) Pro každou komponentu $Q_i$ rozkladu $Q$ platí, že $|Q_i| = 1$.
:::

:::proof

$(1) \implies (2)$:

Buď $Q$ reduktivní, pak platí, že i každý jeho subquandle je reduktivní. Uvažme libovolnou komponentu $Q_i$ rozkladu $Q$. Jelikož je $Q_i$ souvislý, ale i reduktivní, pak podle @redsou platí, že $|Q_i| = 1$.

$(2) \implies (1)$:

Uděláme to indukcí podle podle velikosti $Q$. Pro $|Q| = 1$ tvrzení platí triviálně.
Na $Q$ budeme působit grupou $\Inn{Q}$. Orbity jsou podquandly, pro něž víme, že jejich komponenty mají velikost $1$. Podle indukčního předpokladu tedy víme, že jsou reduktivní, a tedy i lokálně reduktivní. Podle lemmatu @pumping pak plyne, že i $Q$ je lokálně reduktivní. Nyní aplikujeme @local a dostaneme, že $Q$ je reduktivní.
:::

## Charakterizace triviálních barvení

:::{.veta #stuha}
Pro každý souvislý quandle $Q$, $|Q| > 1$ existuje takový uzel $K$, že $\Col{Q}{K} > |Q|$.
:::

:::proof
Pro důkaz této věty použijeme konstrukci, která se poprvé objevila v článku [@johnson1980homomorphs], a kterou si upravíme tak, aby řešila náš problém. Konstrukce je následující:

Nejprve uvažujme orientovaný $m$-link, $m = |Q|$, takový, že každou komponentu obarvíme jiným prvkem z $Q$. Následně budeme postupně propojovat pomocí pásků tak dlouho, dokud nám nevznikne uzel. Na konci dostaneme uzel, který bude mít netriviální obarvení, jelikož každá komponenta bude obarvena jiným prvkem z $Q$. Pak bude platit, že $\Col{Q}{K} > |Q|$.

![$m$-link](../img/link.pdf)

Mějme zadaný souvislý quandle $Q$. Jelikož je $Q$ souvislý, pak podle lemmatu @conn existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b,$$

pro každé dva prvky $a, b \in Q$.

Začněme s komponentou obarvenou prvkem $a$. Z ní povedeme pásek. Pokud pásek bude křižovat s nějakou jinou komponentou, tak budeme postupovat podle jedné z následujících situací:

1) Pokud se pásek kříží s komponentou obarvenou prvkem $c \neq x_1$ pak pásek povedeme pod celou komponentou. Dojde tedy k situaci na obrázku \ref{under}. Tedy pásek povedeme pod celou komponentou, aniž bychom změnili obarvení konec pásku.

![Pásek pod komponentou](../img/under.pdf){#under}

2) Pokud se pásek kříží s komponentou obarvenou prvkem $c = x_1$ a platí, že $\varepsilon_1 = 1$, pak pásek provlékneme skrz tuto komponentu způsobem jako na obrázku \ref{through}. Konec pásku bude obarvený prvkem $x_1 * a$, zatímco komponenta obarvená prvkem $x_1$ zůstane nezměněná.

![$x_1 * a$](../img/through.pdf){#through}

3) Pokud se pásek kříží s komponentou obarvenou prvkem $c = x_1$ a platí, že $\varepsilon_1 = -1$, pak pásek provlékneme skrz tuto komponentu způsobem jako na obrázku \ref{through_inv}. Konec pásku bude obarvený prvkem $x_1 *^{-1} a$, zatímco komponenta obarvená prvkem $x_1$ zůstane nezměněná.

![$x_1 *^{-1} a$](../img/through_inv.pdf){#through_inv}

Tento způsob budeme opakovat pro konec pásku tak dlouho, dokud konec pásku nebude obarvený prvkem $b$. Jelikož je posloupnost $x_1, x_2, \dots x_n$ konečná, tak k němu opravdu dojdeme. Následně pásek připojíme na komponentu obarvenou prvkem $b$.

Počet komponent je konečný a jednou iterací algoritmu jsme snížili počet komponent o jedna. Algoritmus budeme tedy opakovat tak dlouho, dokud nedostaneme uzel. Takový uzel nazývá *stuhový uzel* (anglicky *ribbon knot*). Jelikož jsme každou komponentu $|Q|$-linku obarvili jiným prvkem z $Q$ a algoritmus toto obarvení zachovává, dostaneme uzel, který bude mít netriviální obarvení. Tedy $\Col{Q}{K} > |Q|$.
:::

:::{.veta #valoun}
Mějme konečný quandle $Q$. Pak platí, že $\Col{Q}{K}$ je konstantní, právě tehdy když je $Q$ reduktivní.
:::

:::proof
Pokud je $Q$ souvislý, tak z předpokladu víme, že $|Q| > 1$. Pak podle věty @stuha zkonstruujeme příslušný stuhový uzel $K$ tak, že bude mít netriviální obarvení $\Col{Q}{K} > |Q|$. Tedy není konstantní.

Jestliže $Q$ není souvislý, pak se $Q$ podle věty @rozklad rozkládá na komponenty $(Q_1, Q_2, \dots, Q_n)$. Z předpokladu víme, že existuje komponenta $Q_i$ taková, že $|Q_i| > 1$. Označme si $Q_i$ jako $W$.
Pak podle @stuha platí, že $\Col{W}{K} > |W|$. Jelikož $W \preccurlyeq Q$, tak podle lemmatu @suma platí, že $\Col{Q}{K} \geq \Col{W}{K} - |W| + |Q| > |Q|$. A tedy není konstantní.

Naopak, pokud platí, že $Q$ je reduktivní, pak podle lemmatu @hom platí, že jedinými homomorfismy z $Q_K$ do $Q$ jsou takové, že jejich obraz je triviální. Tedy platí, že $\Col{Q}{K} = |Q|$, a tudíž $\Col{Q}{K}$ je konstantní pro všechny uzly $K$.
:::

# Barvení jako Vassilievův invariant

V článku [@eisermann1999number] se autor zabývá otázkou, zda je počet grupových homomorfismů z fundamentální grupy do zvolené grupy $G$ Vassilievův invariant. Jeho výsledkem je charakterizace, že pokud je $G$ nilponentní, tak je počet homomorfismů konstantní, jinak není Vassilievův invariant. V tété kapitole se pokusíme zobecnit tento výsledek na quandle.

Motivací je, že fundamentální quandle je úplný invariant, tedy plně charakterizuje uzel. Zároveň platí, že grupové homomorfismy mají svojí representaci i jako quandleové homomorfismy, ovšem ne každý quandleový homomorfismus má svojí reprezentaci jako grupový homomorfismus. Tedy pokud bychom dokázali obdobný výsledek pro quandleové homomorfismy, tak bychom mohli získat silnější výsledek, než který je v původním článku.

## Barvení uzlů

:::{.veta #omezeni}
[@eisermann1999number].
Buď $s(K)$ copánkový index uzlu $K$. Pak pokud invariant $v: \mathcal{K} \rightarrow \mathbb{C}$ splňuje, že $|v(K)| \leq f(s(K))$ pro nějakou funkci $f: \mathbb{N} \rightarrow \mathbb{N}$ a pro všechny uzly $K \in \mathcal{K}$, pak $v$ není Vassilievův invariant, nebo je konstantní.
:::

:::{.veta #kukurice}
Pro každý quandle $Q$ platí, že počet obarvení $\Col{Q}{K}$ není Vassilievův invariant, nebo je konstantní.
:::

:::proof
Mějme fixně zadaný quandle $Q$ a pro něj uvažujme libovolný uzel $K$ a jeho minimální copánkovou reprezentaci odpovídající copánkovému indexu $s(K)$. Pak platí, že máme-li konkrétní obarvení $f \in \text{Hom}(Q_K, Q)$, tak je jednoznačně určeno obarvením konců provázků v copánkové reprezentaci. Tedy platí, že $\Col{Q}{K}$ dokážeme omezit tak, že každému konci přiřadíme nějaký prvek z $Q$. Tedy

$$\Col{Q}{K} \leq |Q|^{s(K)}.$$

Použitím věty @omezeni dostáváme, že $\Col{Q}{K}$ není Vassilievův invariant, nebo je konstantní.
:::

:::dusledek
Mějme quandle $Q$. Pak platí, že není Vassilievův invariant, právě tehdy když není reduktivní.
:::

:::proof
Z věty @valoun plyne, že $\Col{Q}{K}$ není konstantní, právě tehdy když $Q$ není reduktivní. Z věty @kukurice plyne, že $\Col{Q}{K}$ není Vassilievův invariant, právě tehdy když není konstantní. Tedy obě tvrzení jsou ekvivalentní.
:::

:::dusledek
Mějme grupu $G$. Pak platí, že následující tvrzení jsou ekvivalentní:

1) $G$ je nilpotentní;

2) quandle $\Conj{G}$ je reduktivní.
:::

:::proof
V článku @eisermann1999number bylo obdobným způsobem dokázáno, že grupa $G$ je nilpotentní, právě tehdy když počet homomorfismů z fundamentální grupy uzlu do $G$ je konstantní. Naopak z věty @valoun plyne, že quandle $\Conj{G}$ je reduktivní, právě tehdy když počet obarvení uzlu quandlem $\Conj{G}$ je konstantní. Tedy obě tvrzení jsou ekvivalentní.
:::

## Barvení linků

Obdobnou charakterizaci můžeme získat i pro linky. Ovšem, v tomto případě bude vše jednodušší.

:::veta
Uvažujme quandle $Q$ a link $L$ s alespoň 2 komponentami. Pak platí, že $\text{Col}_Q(L)$ není Vassilievův invariant, nebo je konstantní. Navíc $\text{Col}_Q(L)$ je konstantní, právě tehdy když $Q$ je trivialní quandle.
:::

:::proof
První část je jen variací věty @kukurice, kde místo uzlu uvažujeme link.

Dále, pokud je $Q$ triviální quandle, tak jak platí, že $\text{Col}_Q(L) = |Q|^l$, kde $l$ je počet komponent linku $L$. Tedy $\text{Col}_Q(L)$ je konstantní pro všechny linky $L$ s $l$ komponentami.

Naopak Uvažujme quandle $Q$, který není triviální. Pak jako $L$ označíme $2$-link a jako $H$ hopf link. 

Pro $L$ platí, že $\text{Col}_Q(L) = |Q|^2$ pro všechny quandly $Q$.

Jelikož $Q$ není trivialní, tak existuje dvojice prvků $a, b \in Q$ taková, že $a \neq b$ a $a * b \neq b$. Pokud obarvíme $H$ tak, že první komponentu obarvíme prvkem $a$ a druhou komponentu obarvíme prvkem $b$, tak ze vztahu výše plyne, že $H$ nejde touto dvojicí prvků obarvit. Tedy $\text{Col}_Q(H) < |Q|^2$. Tedy $\text{Col}_Q$ není konstantní.
:::
