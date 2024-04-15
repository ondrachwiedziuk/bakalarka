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
# Quandly

Quandle vznikl jako algebraická struktura, která respektuje Reidemeisterovy pohyby, a je tak vhodná pro rozlišování uzlů. V této kapitole rozvinu základní teorii kolem těchto algebraických struktur.

:::definice
*Quandlem* $Q = (C, *)$ rozumíme algebraickou strukturu nad množinou $C$ s binární operací $*$, splňující následující podmínky pro všechna $a, b, c \in C$:

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

Na quandlech bychom nyní zavedli základní pojmy běžné i pro jiné algebraické struktury, jako homomorfismy, podalgebry a faktoralgebry běžné v univerzální algebře. Pomocí nich si pak můžeme lépe porozumět vlastnostem quandlů.

:::definice
Mějme quandly $Q$ a $W$. Pak *quandlovým homomorfismem* $\varphi: Q \rightarrow W$ rozumíme zobrazení, které zachovává quandlovou operaci, tedy $\varphi(a * b) = \varphi(a) * \varphi(b)$ pro všechna $a, b \in Q$.
:::

:::definice
Mějme quandle $(Q, *)$. Pak *podquandlem* $W \preccurlyeq Q$ rozumíme dvojici $(W, *|_W)$, kde $W \subseteq Q$ a platí, že $W$ je uzavřená na operaci $*$ jakožto zúžení operace z $Q$.
:::

:::definice
Buď $Q$ quandle. Na něm zavedeme relaci ekvivalence $\alpha$ takovou, že $[a]_\alpha * [b]_\alpha = [a * b]_\alpha$ pro všechna $a, b \in Q$. Vzniklý quandle definovaný na blocích ekvivalence značíme $\quot{Q}{\alpha}$ a nazýváme *faktorquandlem* quandlu $Q$ podle ekvivalence $\alpha$.
:::

Víme, že $a \mapsto [a]_\alpha$ je homomorfismus z $Q$ na $\quot{Q}{\alpha}$. Také platí, že pokud máme homomorfismus $\varphi: Q \rightarrow W$, pak jádro, tj množina $\Ker \varphi = \{ (a, b) \in Q \times Q: \varphi(a) = \varphi(b) \}$, tvoří kongruenci na $Q$ a faktorquandle $\quot{Q}{\Ker \varphi}$ je izomorfní s obrazem $\Ima \varphi(Q) \preccurlyeq W$. Jedná se o klasický výsledek univerzální algebry, který můžeme nalézt např. v knize [@Jezek2008]. Dalším takovým výsledkem je, že kongruence tvoří svaz:

:::definice
Kongruence $\alpha$ tvoří svaz, který značíme $\Con{Q}$. Minimální prvek tohoto svazu značíme $0_Q$ a je definován jako $\{ (a, a): a \in Q \}$. Maximální prvek značíme $1_Q$ a je definován jako $Q \times Q$.
:::

Nyní tyto pojmy využijeme, abychom definovali fundamentální quandle. Ten je základním nástrojem pro studium barvení uzlů.

:::definice
*Volným quandlem* $Q_X$ nad neprázdnou množinou $X$ rozumíme quandle takový, že pro zobrazení $f: X \rightarrow Q$, kde $Q$ je libovolný quandle, existuje právě jeden homomorfismus $\varphi: Q_X \rightarrow Q$ takový, že $\varphi(x) = f(x)$ pro všechna $x \in X$.
:::

:::definice
Mějme $K$ uzel, $D_K$ jeho diagram, pak *fundamentálním quandlem* $Q_K$ rozumíme volný quandle nad množinou oblouků $O(D_K)$ vyfaktorizovaný relacemi dané kříženími $C(D_K)$ takové, že pro každé křížení $(a, b, c) \in C(D_K)$ platí $a * b = c$.
:::

:::tvrzenic
[@Joyce1982ACI].
Fundamentální quandle $Q_K$ je úplným invariantem až na orientaci.
:::

Fundamentální quandle dává sice velmi silný invariant, ale je těžké ho spočítat. Fundamentální quandle je nekonečný a určit, zda jsou dva takové quandly izomorfní, je velmi obtížné. Proto se spíše používá z něj odvozený invariant, kterému se říká *quandlové barvení*. Jedná se homomorfismus z fundamentálního quandlu do námi zvoleného konečného quandlu. Tento invariant je sice slabší, ale lze mnohem snadněji spočítat. Dále lze odvodit další invariant a to počet takových homomorfismů.

:::definice
Mějme uzel $K$, jeho fundamentální quandle $Q_K$ a libovolný quandle $W$. Pak *počtem obarvení* $\Col{W}{K}$ rozumíme počet homomorfismů $\varphi: Q_K \rightarrow W$. Tedy $\Col{W}{K} = |\Hom{Q_K}{W}|$.
:::

![Barvení pomocí quandlu](../img/coloring.pdf)

Jak takový invariant funguje, si ukážeme na příkladu *Foxova quandlu*. Začneme definicí tohoto quandlu. Originálně je Foxovo barvení definováno jako barvení oblouků jednou ze tří barev tak, aby na každém křížení byly měly všechny tři oblouky buď stejnou barvu, nebo navzájem různou. Nyní si reformulujme toto barvení jako homomorfismus z fundamentálního quandlu do Foxova quandlu. Foxův quandle $F$ definujeme následující tabulkou:

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

Nyní si zvolme uzel $K$ a jeho fundamentální quandle $Q_K$. Pro každý oblouk $a \in O(D_K)$ si zvolme jeden z prvků $f(a) \in F$ tak, abychom dostali homomorfismus $f: Q_K \rightarrow F$. Jelikož je fundamentální quandle $Q_K$ definovaný na obloucích diagramu, tak každý homomorfismus lze vyjádřit tímto způsobem. Naopak ne pro každé přiřazení prvků $f(a)$ dostaneme homomorfismus. Pro náš případ si všimneme, že pro křížení $(a, b, c)$ platí, že když $f(a) = f(b)$, pak i $f(c) = f(a)$. Naopak, pokud $f(a) \neq f(b)$, tak $f(c) \neq f(a), f(b)$, což nám dává přesně pravidla Foxova barvení.

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

(2) $\Rightarrow$ (1): Jelikož každé dva prvky dokážeme spojit konečnou posloupností prvků, tak platí, že grupa $G$ daná levými translacemi $\Inn{Q}$ působí tranzitivně na $Q$. Tudíž je $Q$ souvislý.
:::

:::{.lemma #orbita}
Mějme quandle $Q$ a grupu vnitřních automorfismů $\Inn{Q}$. Pak platí, že působení $\Inn{Q}$ na $Q$ rozkládá $Q$ na orbity a každá orbita je podquandle.
:::

:::proof
Zafixujme si orbitu nějakou $W$. Tak platí, že $W$ je uzavřená na operaci $*$, jelikož pokud $a, b \in W$, tak $a * b = L_a(b) \in W$. Zároveň je uzavřená na levé dělení, jelikož pokud $a, b \in W$, tak $a *^{-1} b = L_a^{-1}(b) \in W$. Tedy $W$ je podquandle.
:::

:::priklad
Mezi souvislé quandly patří např. foxův quandle $F$. Naopak, mezi nesouvislé patří triviální quandly $T_n$, kde $n > 1$. Tyto quandly se rozpadnou na $n$ jednoprvkových podquandlů $T_1$, který je ale triviálně souvislý.
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
Mějme quandle $Q$. Pak *rozkladem* quandle $Q$ rozumíme rozklad na souvislé podquandly $(Q_1, Q_2, \dots, Q_n)$. Subquandle $Q_i$ nazýváme *komponenta* $Q$.
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
Mějme $a, b \in Q_K$ generátory. Pak chceme ověřit, že existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q_K$ taková, že $x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b$. Jenže, jelikož jsou $a, b$ generátory, tak odpovídají nějakým obloukům $a', b' \in O(D_K)$. Posloupnost prvků $x_1, x_2, \dots, x_n$ pak dostaneme tak, že začneme v $a'$ a budeme ve směru k $b'$. Pokaždé, když narazíme na křížení, kde je $x_i'$ most, tak si přidáme $x_i$ do posloupnosti s příslušným znaménkem operace. Jelikož $a, b$ leží na stejném uzlu, tak se tímto způsobem dostaneme z $a$ do $b$.

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

## Reduktivita

V této sekci se budeme zabývat reduktivními quandly. Tyto quandly jsou studovány v článcích [@bonatto2020quandles], [@bonatto2021universal] a [@Jedlicka2020]. Ovšem jejich motivace při definici reduktivity je čistě algebraická. My se budeme zabývat reduktivitou ve vztahu k uzlům a jejich barvením. V této kapitole vycházím primárně z prvního zmíněného článku.

:::definice
Buď $n \in \N$. Pak quandle $Q$ nazýváme *$n$-reduktivní*, pokud platí, že všechny $a, b, c_1, c_2, \dots, c_n \in Q$ splňují:

$$((\dots(a * c_1) \dots) * c_{n-1}) * c_n = ((\dots(b * c_1)\dots) * c_{n-1}) * c_n$$.

Říkáme, že $Q$ je *reduktivní*, pokud existuje $n \in \N$, že je $n$-reduktivní.
:::

:::definice
Buď $Q$ quandle. Pak definujeme grupu $\text{Trans}_\alpha = \langle L_a L_b^{-1} : a\, \alpha\, b \rangle \trianglelefteq \Inn{Q}$. Tato grupa se nazývá *transvekční grupa* quandlu $Q$ podle relace ekvivalence $\alpha$.
:::

:::{.lemma #trans}
Buď $Q$ quandle. Pak jsou orbity působení $\Inn{Q}$ na $Q$ a transvekční grupy $\text{Trans}_{1_Q}$ na $Q$ shodné.
:::

:::definice
Buď $Q$ quandle. Pak definujeme $\Orb{\text{Trans}_\alpha}$ jako množinu $\{ (a, b) \in Q \times Q: \varphi(a) = b, \varphi \in \text{Trans}_\alpha \}$. Dále definujme $\Orb[n+1]{Q} = \Orb{\text{Trans}_{\Orb[n]{Q}}}$.
:::

Jedná se o trochu robustnější definici rozkladu na souvislé komponenty, která nám umožňuje s nimi lépe pracovat za pomocí kongruencí.

:::{.lemma #blivajz}
Technické lemma z [@bonatto2020quandles].
:::

:::{.tvrzenic #redbar}
[@bonatto2020quandles].
Buď $Q$ konečný quandle. Pak jsou následující podmínky ekvivalentní:

1) $Q$ je reduktivní.

2) $\Orb[n]{Q} = 0_Q$ pro nějaké $n \in \N$.

3) Pro každou komponentu $Q_i$ rozkladu $Q$ platí, že $|Q_i| = 1$.
:::

:::proof
$(1) \implies (2)$:

$(2) \implies (1)$:

$(2) \implies (3)$:

Vidíme, že $\Orb[n]{Q}$ odpovídá tomu, že budeme postupně rozkládat $Q$ na menší a menší orbity, až dosáhneme rozkladu na souvislé komponenty. Jelikož $\Orb[n]{Q} = 0_Q$, tak všechny komponenty mají velikost $1$.

$(3) \implies (2)$:

Pokud všechny komponenty rozkladu mají velikost $1$, tak to znamená, že existuje $n \leq |Q|$ takové, že $\Orb[n]{Q} = 0_Q$, protože $Q$ je konečný quandle.
:::

:::{.dusledek #redsou}
Jediný souvislý reduktivní quandle je triviální quandle velikosti $1$.
:::

<!-- :::definice
Buď $Q$ quandle. Pak *lokálně $n$-reduktivním* quandlem rozumíme takový quandle, že pro každé $a, b \in Q$ platí rovnost:

$$((\dots(a *\underbrace{b) \dots) * b) * b}_n = b$$,

Říkáme, že $Q$ je *lokálně reduktivní*, pokud je lokálně $n$-reduktivní pro nějaké $n \in \N$.
:::

:::{.lemma #pumping}
Pokud všechny orbity jsou lokálně $n$-reduktivní, tak je quandle lokálně $n+1$-reduktivní.
:::

:::proof
Mějme quandle $\Orb{Q}$. Víme, že pro každý vnitřní automorfismus $\varphi \in \Inn{Q}$ platí, že $[\varphi(a)] = [a]$ pro všechna $[a] \in \Orb{Q}$. Tedy $\Orb{Q}$ je triviální quandle, který je $1$-reduktivní.

Dále mějme nějaké $[a] \in \Orb{Q}$ a $b \in Q$. Pak platí, že

$$[a * b] = [a] * [b] = [b]$$.

Jelikož orbita $b$ je lokálně $n$-reduktivní, tak z toho už plyne, že:

$$((\dots(a *\underbrace{b) \dots) * b) * b}_{n+1} = b$$,

protože tím prvním krokem se dostaneme do orbity, ve které je $b$, a v ní už uplatníme lokální reduktivitu. Tedy $Q$ je lokálně $n+1$-reduktivní.
:::

:::{.veta #local}
Pro konečné quandly platí, že je lokálně reduktivní, právě tehdy když je reduktivní.
:::

:::pozn
Dost těžký dokázat, používá se dost pokročilá teorie grup. Má cenu to zde dokazovat?
:::

:::{.lemma #redsou}
Jediný souvislý reduktivní quandle je triviální quandle velikosti $1$.
:::

:::proof
Mějme souvislý reduktivní quandle $Q$, ten je i lokálně reduktivní. tedy máme, že pro každé $a, b \in Q$ platí, že

$$((\dots(a *\underbrace{b) \dots) * b) * b}_n = b$$.

Jelikož je $Q$ souvislý, pak existuje $L \in \Inn{Q}$ takové, že $L(a) = b$. Pak působením $L$ dostaneme, že
:::

:::tvrzeni
Buď $Q$ quandle. Pak jsou následující podmínky ekvivalentní:

1) $Q$ je reduktivní.

2) Pro každou komponentu $Q_i$ rozkladu $Q$ platí, že $|Q_i| = 1$.
:::

:::proof

$(1) \implies (2)$:

Buď $Q$ reduktivní, pak platí, že i každý jeho subquandle je reduktivní. Uvažme libovolnou komponentu $Q_i$ rozkladu $Q$. Jelikož je $Q_i$ souvislý, ale i reduktivní, pak podle \ref{redsou} platí, že $|Q_i| = 1$.

$(2) \implies (1)$:

Uděláme to indukcí podle podle velikosti $Q$. Pro $|Q| = 1$ tvrzení platí triviálně.
Na $Q$ budeme působit grupou $\Inn{Q}$. Orbity jsou podquandly, pro něž víme, že jejich komponenty mají velikost $1$. Podle indukčního předpokladu tedy víme, že jsou reduktivní, a tedy i lokálně reduktivní. Podle lemmatu \ref{pumping} pak plyne, že i $Q$ je lokálně reduktivní. Nyní aplikujeme \ref{local} a dostaneme, že $Q$ je reduktivní.
::: -->
