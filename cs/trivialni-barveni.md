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
# Trivální barvení

## Reduktivita

:::definice
Buď $n \in \N$. Pak quandle $Q$ nazýváme *$n$-reduktivní*, pokud platí, že všechny $a, b, c_1, c_2, \dots, c_n \in Q$ splňují:

$$((\dots(a * c_1) \dots) * c_{n-1}) * c_n = ((\dots(b * c_1)\dots) * c_{n-1}) * c_n$$.

Říkáme, že $Q$ je *reduktivní*, pokud existuje $n \in \N$, že je $n$-reduktivní.
:::

:::definice
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
:::

## Charakterizace triviálních barvení

:::{.veta #stuha}
Pro každý souvislý quandle $Q$, $|Q| > 1$ existuje takový uzel $K$, že $\Col{Q}{K} > |Q|$.
:::

:::proof
Pro důkaz této věty použijeme konstrukci, která se poprvé objevila v článku [@johnson1980homomorphs], a kterou si upravíme tak, aby řešila náš problém. Konstrukce je následující:

Nejprve uvažujme orientovaný $m$-link, $m = |Q|$, takový, že každou komponentu obarvíme jiným prvkem z $Q$. Následně budeme postupně propojovat pomocí pásků tak dlouho, dokud nám nevznikne uzel. Na konci dostaneme uzel, který bude mít netriviální obarvení, jelikož každá komponenta bude obarvena jiným prvkem z $Q$. Pak bude platit, že $\Col{Q}{K} > |Q|$.

![$m$-link](../img/link.pdf)

Mějme zadaný souvislý quandle $Q$. Jelikož je $Q$ souvislý, pak podle lemmatu \ref{conn} existuje konečná posloupnost prvků $x_1, x_2, \dots, x_n \in Q$ taková, že

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
Pokud je $Q$ souvislý, tak z předpokladu víme, že $|Q| > 1$. Pak podle věty \ref{stuha} zkonstruujeme příslušný stuhový uzel $K$ tak, že bude mít netriviální obarvení $\Col{Q}{K} > |Q|$. Tedy není konstantní.

Jestliže $Q$ není souvislý, pak se $Q$ podle věty \ref{rozklad} rozkládá na komponenty $(Q_1, Q_2, \dots, Q_n)$. Z předpokladu víme, že existuje komponenta $Q_i$ taková, že $|Q_i| > 1$. Označme si $Q_i$ jako $W$.
Pak podle \ref{stuha} platí, že $\Col{W}{K} > |W|$. Jelikož $W \preccurlyeq Q$, tak podle lemmatu \ref{suma} platí, že $\Col{Q}{K} \geq \Col{W}{K} - |W| + |Q| > |Q|$. A tedy není konstantní.

Naopak, pokud platí, že $Q$ je reduktivní, pak podle lemmatu \ref{hom} platí, že jedinými homomorfismy z $Q_K$ do $Q$ jsou takové, že jejich obraz je triviální. Tedy platí, že $\Col{Q}{K} = |Q|$, a tudíž $\Col{Q}{K}$ je konstantní pro všechny uzly $K$.
:::