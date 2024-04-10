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
# Quandly

Quandle vznikl jako algebraická struktura, která respektuje Reidemeisterovy pohyby, a je tak vhodná pro rozlišování uzlů. V této kapitole rozvinu základní teorii kolem těchto algebraických struktur.

:::definice
*Quandlem* $Q = (C, *)$ rozumíme algebraickou strukturu nad (konečnou) množinou $A$ s binární operací $*$, splňující následující podmínky pro všechna $a, b, c \in C$:

1) $a * a = a$ (idempotence);

2) $\exists! x \in C: a * x = b$ (jednoznačné levé dělení, značíme $x = a *^{-1} b$);

3) $a*(b*c) = (a*b)*(a*c)$ (levá samodistributivita).
:::

:::priklad
Příkladem quandle je například *triviální jednoprvkový quandle* $Q = (\{ a \}, *)$, kde $a * a = a$. Značme ho jako $T_1$. *Trivální quandle* nad $A$ definujeme tak, že vezmeme množinu $A$ a definujeme $a * b = b$ pro všechna $a, b \in A$. Takový quandle značíme $T_A$.
:::

:::priklad
Dalším příkladem může být quandle daný konjugací v grupě $G$. Pro $a, b \in G$ definujeme $a * b = a b a^{-1}$. Tento quandle značíme $\Conj{G}$.
:::

Na quandlech bychom zavedli základní pojmy běžné i pro jiné algebraické struktury, jako homomorfismy, podalgebry a faktoralgebry běžné v univerzální algebře. Pomocí nich si pak můžeme lépe porozumět vlastnostem quandlů.

:::definice
Mějme quandly $Q$ a $W$. Pak *quandlovým homomorfismem* $\varphi: Q \rightarrow W$ rozumíme zobrazení, které zachovává quandlovou operaci, tedy $\varphi(a * b) = \varphi(a) * \varphi(b)$ pro všechna $a, b \in Q$.
:::

:::definice
Mějme quandle $(Q, *)$. Pak *podquandlem* $W$ rozumíme dvojici $(W, *|_W)$, kde $W \subseteq Q$ a platí, že $W$ je uzavřená na operaci $*$ jakožto zúžení operace z $Q$. Vztah značíme $W \preccurlyeq Q$.
:::

:::definice
Buď $Q$ quandle. Na něm zavedeme relaci ekvivalence $\alpha$ takovou, že $[a]_\alpha * [b]_\alpha = [a * b]_\alpha$ pro všechna $a, b \in Q$. Vzniklý quandle definovaný na blocích ekvivalence značíme $\quot{Q}{\alpha}$ a nazýváme *faktorquandlem* quandlu $Q$ podle ekvivalence $\alpha$.
:::

Víme, že $a \mapsto [a]_\alpha$ je homomorfismus z $Q$ na $\quot{Q}{\alpha}$. Také platí, že pokud máme homomorfismus $\varphi: Q \rightarrow W$, pak jádro, tj množina $\Ker \varphi = \{ (a, b) \in Q \times Q: \varphi(a) = \varphi(b) \}$, tvoří kongruenci na $Q$ a faktorquandle $\quot{Q}{\Ker \varphi}$ je izomorfní s obrazem $\Ima \varphi(Q) \preccurlyeq W$. Jedná se o klasický výsledek univerzální algebry.

Nyní tyto pojmy využijeme, abychom definovali fundamentální quandle. Ten je základním nástrojem pro studium barvení uzlů.

:::definice
*Volným quandlem* $Q_X$ nad neprázdnou množinou $X$ rozumíme quandle takový, že pro zobrazení $f: X \rightarrow Q$, kde $Q$ je libovolný quandle, existuje právě jeden homomorfismus $\varphi: Q_X \rightarrow Q$ takový, že $\varphi(x) = f(x)$ pro všechna $x \in X$.
:::

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram, pak *fundamentálním quandlem* $Q_K$ rozumíme volný quandle nad množinou oblouků $O(D_K)$ vyfaktorizovaný relacemi dané kříženími $C(D_K)$ takové, že pro každé křížení $(a, b, c) \in C(D_K)$ platí $a * b = c$.
:::

:::tvrzeni
[@Joyce1982ACI].
Fundamentální quandle $Q_K$ je úplným invariantem až na orientaci.
:::

Fundamentální quandle dává sice velmi silný invariant, ale je těžké ho spočítat. Fundamentální quandle je nekonečný a určit, zda jsou dva takové quandly izomorfní, je velmi obtížné. Proto se spíše používá z něj odvozený invariant, kterému se říká *quandlové barvení*. Jedná se homomorfismus z fundamentálního quandlu do námi zvoleného konečného quandlu. Tento invariant je sice slabší, ale lze mnohem snadněji spočítat. Dále lze odvodit další invariant a to počet takových homomorfismů.

:::definice
Mějme uzel $K$, jeho fundamentální quandle $Q_K$ a libovolný quandle $W$. Pak *počtem obarvení* $\Col{W}{K}$ rozumíme počet homomorfismů $\varphi: Q_K \rightarrow W$. Tedy $\Col{W}{K} = |\Hom{Q_K}{W}|$.
:::

Jak takový invariant funguje, si ukážeme na příkladu *Foxova quandlu*. Začneme definicí tohoto quandlu. Originálně je Foxovo barvení definováno na diagramu tak, že každému oblouku přiřadíme jednu ze tří barev tak, aby na každém přížení byly všechny tři barvy, nebo právě jedna. Nyní si reformulujme toto barvení jako homomorfismus z fundamentálního quandlu do Foxova quandlu. Foxův quandle $F$ definujeme následující tabulkou:

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

Nyní si zvolme uzel $K$ a jeho fundamentální quandle $Q_K$. Pro každý oblouk $a \in O(D_K)$ si zvolme jeden z prvků $f(a) \in F$ tak, abychom dostali homomorfismus $f: Q_K \rightarrow F$. Jelikož je fundamentální quandle $Q_K$ definovaný na obloucích diagramu, tak každý homomorfismus lze vyjádřit tímto způsobem. Naopak ne pro každé přiřazení prvků $f(a)$ dostaneme homomorfismus.

![Barvení pomocí quandlu](../img/coloring.pdf)

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

:::definice
Mějme quandle $Q$. Pak $\Orb{Q}$ značíme faktorquandle $Q/\alpha$, kde $\alpha$ je kongruence taková, že $a \alpha b$ právě tehdy, když $a$ a $b$ leží ve stejné orbitě působení $\Inn{Q}$.
:::

:::{.tvrzeni #rozklad}
[@ehrman2006toward].
Mějme quandle $Q$. Pak platí, že se dá jednoznačně rozložit na maximální souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$.
:::

:::proof
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Podle lemmatu \ref{orbita} platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle. Jelikož je $Q$ konečný, tak má konečně mnoho orbit. Pokud je orbita souvislá, tak jsme skončili. Pokud ne, znovu aplikujeme lemma \ref{orbita}. Takto pokračujeme, dokud nedostaneme rozklad na souvislé podquandly. Jelikož je $Q$ konečný a velikost orbit se zmenšuje, tak se vždy dostaneme do souvislého podquandlu.

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
Mějme $a, b \in Q$ ve stejné komponentě. Pak podle lemmatu \ref{conn} existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že 

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
Mějme homomorfismus $\varphi \in \text{Hom}(Q_K, Q)$. Jelikož je $Q_K$ podle \ref{sofun} souvislý, tak podle lemmatu \ref{hom} platí, že $\varphi(Q_K)$ je souvislý podquandle $Q$. Jelikož se $Q$ rozkládá na komponenty, které jsou souvislé, tak platí, že $\varphi$ náleží do $\text{Hom}(Q_K, Q_i)$ pro nějaké $i$. Zároveň patří nejvýše do jedné takové množiny, jelikož jsou orbity disjunktní. Jelikož je $\varphi$ libovolný, tak platí, že

$$\Col{Q}{K} = \sum_{i=1}^n |\text{Col}_{Q_i}(K)|.$$
:::