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
*Uzlem* rozumíme lomenou uzavřenou jednoduchou křivku $K$ vnořenou do prostoru $\R^3$. Množinu všech takových uzlů značíme $\mathbb{K}$.
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
Mějme množinu všech uzlů $\mathbb{K}$ a libovolnou množinu $A$. Pak *invariantem* rozumíme takové zobrazení $I: \mathbb{K} \rightarrow A$, že pokud $K_1 \cong K_2$, pak $I(K_1) = I(K_2)$ pro všechny takové uzly $K_1, K_2 \in \mathbb{K}$.
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

Mějme copánkovou grupu $B_n$ . Pak *uzávěrem* $b \in B_n$ rozumíme uzel $K_b$ takový, který vznikne z $b$ tak, že konce šňůrek přilepíme k sobě tak, že $i$-tá šňůrka zhora se přilepí k $i$-té šňůrce zdola. Tímto způsobem nevznikne vždy uzel podle naší definice, ale obecně vznikne něco, co se nazývá v angličtině *link*, tedy vnoření několika uzlů do stejného prostoru.

![Lepení copánku](../img/glue.pdf)

:::veta
(Alexanderova věta).
Pro každý uzel $K$ existuje takový copánek $b \in B_n$ pro nějaké $n$ takový, že $K$ je ekvivalentní uzávěru $K_b$.
:::

:::definice
Pro daný uzel $K$ rozumíme *copánkovým číslem* $s(K)$ (anglicky *braid index*) nejmenší číslo $n$ takové, že existuje $b \in B_n$ tak, že $K$ je ekvivalentní uzávěru $K_b$.
:::

:::pozorovani
Copánkové číslo $s(K)$ je invariant.
:::

## Quandly

Mezi další invarianty může patřit počet barvení uzlu algebraickou strukturou $Q$ pomocí pravidel odvozených ze zachovávání Reidemeisterových pohybů.

:::definice
*Quandlem* $Q = (C, *)$ rozumíme algebraickou strukturu nad (konečnou) množinou $A$ s binární operací $*$, splňující následující podmínky pro všechna $a, b, c \in C$:

1) $a * a = a$ (idempotence);

2) Existuje právě jedno $x \in C$ splňující $a * x = b$ ;(jednoznačné levé dělení), budeme značit $x = a backslash b$;

3) $a*(b*c) = (a*b)*(a*c)$ (levá samodistributivita).
:::

Barvení uzlu $K$ funguje následujícím způsobem. Nejprve si zvolíme orientaci křivky $K$. Pak každému oblouku $a$ diagramu $D_K$ přiřadíme nějaký prvek $f(a) \in C$ tak, že když procházíme uzel v námi zvoleném směru, tak pokaždé, když narazíme na konec oblouku $a$, tak hodnota navazujícího oblouku $c$ je rovna $f(c) = f(b) * f(a)$, kde $b$ je most v daném křížení. Příslušnou funkci $f$ nazýváme *obarvením* uzlu $K$ quandlem $Q$. Velikost množiny všech takových obarvení pak značíme $\text{Col}_Q(K)$ a jedná se o invariant.

![Barvení pomocí quandlu](../img/coloring.pdf)

Nejlepším invariantem by bylo zadefinovat nějakou ternární relaci na množině oblouků $O(D_K)$ svázaných pomocí množiny křížení $C(D_K)$, ovšem z podmínek daných Reidemeisterovými pohyby plyne, že taková relace je právě quandlem.

Nyní si vybudujeme terminologii tak, abychom mohli výše popsané barvení formálně popsat pomocí algebraické terminologie.

:::definice
Mějme quandly $Q$ a $W$. Pak *homomorfismem* $\varphi: Q \rightarrow W$ rozumíme zobrazení, které zachovává quandlovou operaci, tedy $\varphi(a * b) = \varphi(a) * \varphi(b)$ pro všechna $a, b \in Q$.
:::

:::definice
*Volným quandlem* $Q_X$ nad neprázdnou množinou $X$ rozumíme quandle takový, že pokud máme zobrazení $f: X \rightarrow Q$, kde $Q$ je libovolný quandle, tak existuje právě jeden homomorfismus $\varphi: Q_X \rightarrow Q$ takové, že $\varphi(x) = f(x)$ pro všechna $x \in X$.
:::

<!--

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram. Pak *obarvením* $f: Q \rightarrow O(D_K)$ rozumíme funkci takovou, že každému oblouku $a \in O(D_K)$ přiřadí prvek z $C$ takový, že splňuje $f(b) * f(a) = f(c)$ pro všechny oblouky $a,b,c \in O(D_K)$ takové, že $(a, b, c) \in C(D_K)$. Velikost množiny všech takových obarvení pak značíme $\text{Col}_Q(K)$.
:::


:::tvrzeni
Barvení $\text{Col}_Q(K)$ je invariant.
:::

Otázka zní, jakým quandlem barvit? Můžeme si nějaký pevně zvolit, ovšem můžeme se trefit do takového, že existují jenom triviální barvení. Nebo si můžeme říct, že si sestavíme quandl podle relací daných kříženími.

-->

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram, pak *fundamentálním quandlem* $Q_K$ rozumíme volný quandle nad množinou oblouků $O(D_K)$ modulo relace dané kříženími $C(D_K)$ takové, že pro každé křížení $(a, b, c) \in C(D_K)$ platí $a * b = c$.
:::

:::tvrzeni
Fundamentální quandl $Q_K$ je úplným invariantem.
:::

:::definice
Mějme uzel $K$, jeho fundamentální quandle $Q_K$ a libovolný quandle $W$. Pak *počtem obarvení* $\text{Col}_W(K)$ rozumíme počet homomorfismů $\varphi: Q_K \rightarrow W$.
:::

:::pozorovani
Počet obarvení $\text{Col}_W(K)$ je invariant.
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
