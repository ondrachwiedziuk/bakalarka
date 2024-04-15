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
# Triviální barvení

V předchozí kapitole jsme si ukázali, že homomorfním obrazem fundamentálního quandlu je souvislý quandle. Nyní naopak ukážeme, že pro každý netriviální souvislý quandle existuje takový uzel, který má netriviální obarvení. Na základě toho ukážeme, že quandle dává triviální obarvení pro všechny uzly, právě tehdy když je reduktivní.

:::{.veta #stuha}
Pro každý souvislý quandle $Q$, $|Q| > 1$ existuje takový uzel $K$, že $\Col{Q}{K} > |Q|$.
:::

:::proof
Pro důkaz této věty použijeme konstrukci, která se poprvé objevila v článku [@johnson1980homomorphs], a kterou si upravíme tak, aby řešila náš problém. Konstrukce je následující:

Nejprve uvažujme orientovaný $m$-link, $m = |Q|$, takový, že každou komponentu obarvíme jiným prvkem z $Q$. Následně budeme postupně propojovat pomocí pásků tak dlouho, dokud nám nevznikne uzel. Na konci dostaneme uzel, který bude mít netriviální obarvení, jelikož každá komponenta bude obarvena jiným prvkem z $Q$ a toto obarvení se v průběhu konstrukce zachovává. Z toho pak bude plynout, že $\Col{Q}{K} > |Q|$.

![$m$-link](../img/link.pdf)

Mějme zadaný souvislý quandle $Q$. Jelikož je $Q$ souvislý, pak podle lemmatu \ref{conn} existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že

$$x_1 *^{\varepsilon_1} (x_2 *^{\varepsilon_2} (\dots *^{\varepsilon_{n-1}} (x_n *^{\varepsilon_n} a)) \dots) = b,$$

pro každé dva prvky $a, b \in Q$. Našim cílem bude postupně provádět levé translace $L_{x_1}^{\varepsilon_1}, L_{x_2}^{\varepsilon_2}, \dots, L_{x_n}^{\varepsilon_n}$ tak, abychom na konci mohli propojit dvě komponenty uzlu a získat tak link o $m - 1$ komponentách. Tento postup budeme opakovat tak dlouho, dokud nedostaneme uzel.

Začněme s komponentou obarvenou prvkem $a$. Z ní povedeme pásek. Pokud pásek bude křižovat s nějakou jinou komponentou, tak budeme postupovat podle jedné z následujících situací:

1) Pokud se pásek kříží s komponentou obarvenou prvkem $c \neq x_1$ pak pásek povedeme pod celou komponentou. Dojde tedy k situaci na obrázku \ref{under}. Tedy pásek povedeme pod celou komponentou, aniž bychom změnili obarvení konce pásku i komponenty.

![Pásek pod komponentou](../img/under.pdf){#under}

2) Pokud se pásek kříží s komponentou obarvenou prvkem $c = x_1$ a platí, že $\varepsilon_1 = 1$, pak pásek provlékneme skrz tuto komponentu způsobem jako na obrázku \ref{through}. Konec pásku bude obarvený prvkem $x_1 * a$, zatímco komponenta obarvená prvkem $x_1$ zůstane nezměněná.

![$x_1 * a$](../img/through.pdf){#through}

3) Pokud se pásek kříží s komponentou obarvenou prvkem $c = x_1$ a platí, že $\varepsilon_1 = -1$, pak pásek provlékneme skrz tuto komponentu způsobem jako na obrázku \ref{through_inv}. Konec pásku bude obarvený prvkem $x_1 *^{-1} a$, zatímco komponenta obarvená prvkem $x_1$ zůstane nezměněná.

![$x_1 *^{-1} a$](../img/through_inv.pdf){#through_inv}

Tento způsob budeme opakovat pro konec pásku tak dlouho, dokud konec pásku nebude obarvený prvkem $b$. Jelikož je posloupnost $x_1, x_2, \dots x_n$ konečná, tak k němu opravdu dojdeme. Následně pásek připojíme na komponentu obarvenou prvkem $b$ a tím získáme link o $m - 1$ komponentách.

Počet komponent je konečný a jednou iterací algoritmu jsme snížili počet komponent o jedna. Algoritmus budeme tedy opakovat tak dlouho, dokud nedostaneme uzel. Takový uzel nazývá *stuhový uzel* (anglicky *ribbon knot*). Jelikož jsme každou komponentu $|Q|$-linku obarvili jiným prvkem z $Q$ a algoritmus toto obarvení zachovává, dostaneme uzel, který bude mít netriviální obarvení. Tedy $\Col{Q}{K} > |Q|$.
:::

:::priklad
Nyní provedeme konstrukci pro Foxův quandle $F$. Víme, že $2 * 1 = 3$ a $1 * 2 = 3$. Nejprve propojíme komponenty $1$ a $3$, následně připojíme zbývající komponentu $2$ a dostaneme stuhový uzel $R_F$ jako na obrázku \ref{ribfox}.
:::

![Stuhový uzel pro Foxův quandle](../img/ribfox.pdf){#ribfox}

:::{.veta #valoun}
Mějme konečný quandle $Q$. Pak platí jsou následující tvrzení ekvivalentní:

1) $\Col{Q}{K}$ je konstantní,

2) $Q$ je reduktivní.
:::

:::proof
Pokud je $Q$ souvislý a netriviální, pak podle věty \ref{stuha} zkonstruujeme příslušný stuhový uzel $R$ tak, že bude mít netriviální obarvení $\Col{Q}{R} > |Q|$. Zároveň lze unknot $U$ obarvit triviálně, tedy $\Col{Q}{U} = |Q|$. Tedy $\Col{Q}{K}$ není konstantní.

$(1) \implies (2)$:

Tuto implikaci ukážeme obměnou. Předpokládáme, že $Q$ není reduktivní. $Q$ podle věty \ref{rozklad} rozkládá na komponenty $(Q_1, Q_2, \dots, Q_n)$. Jelikož $Q$ není reduktivní, pak z \ref{redbar} víme, že existuje komponenta $Q_i$ taková, že $|Q_i| > 1$. Označme si $Q_i$ jako $W$.
Pak podle \ref{stuha} platí, že $\Col{W}{K} > |W|$. Jelikož $W \preccurlyeq Q$, tak podle lemmatu \ref{suma} platí, že $\Col{Q}{K} \geq \Col{W}{K} - |W| + |Q| > |Q|$. A tedy není konstantní.

$(2) \implies (1)$:

Jestliže $Q$ je reduktivní, pak z \ref{redbar} platí, že všechny komponenty jsou triviální. Z \ref{hom} plyne, že $\Col{Q}{K} = |Q|$, a tudíž $\Col{Q}{K}$ je konstantní pro všechny uzly $K$.
:::