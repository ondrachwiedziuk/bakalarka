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

## Reduktivita

V této sekci se budeme zabývat reduktivními quandly. Tyto quandly jsou studovány v článcích [@bonatto2020quandles], [@bonatto2021universal] a [@Jedlicka2020]. Ovšem jejich motivace při definici reduktivity je čistě algebraická. My se budeme zabývat reduktivitou ve vztahu k uzlům a jejich barvením. V této kapitole vycházím primárně z prvního zmíněného článku.

:::definice
Buď $n \in \N$. Pak quandle $Q$ nazýváme *$n$-reduktivní*, pokud platí, že všechny $a, b, c_1, c_2, \dots, c_n \in Q$ splňují:

$$((\dots(a * c_1) \dots) * c_{n-1}) * c_n = ((\dots(b * c_1)\dots) * c_{n-1}) * c_n$$.

Říkáme, že $Q$ je *reduktivní*, pokud existuje $n \in \N$, že je $n$-reduktivní.
:::

:::definice
Buď $Q$ quandle. Pak definujeme grupu $\Dis{\alpha} = \langle L_a L_b^{-1} : a\: \alpha\: b \rangle \trianglelefteq \Inn{Q}$. Tato grupa se nazývá *pohybová grupa* quandlu $Q$ podle relace ekvivalence $\alpha$.
:::

Obecně platí, že pohybové grupy $\Dis{\alpha} \trianglelefteq \Inn{Q}$. Toho využijeme při definici kongruence na quandlech.

:::definice
Buď $Q$ quandle a $N \trianglelefteq \Inn{Q}$. Pak definujeme $\Orb{N} = \{ (a, b) \in Q \times Q: \varphi(a) = b, \varphi \in N \}$.
:::

Pokud budeme volit $N = \Dis{\alpha}$, kde $\alpha \in \Con{Q}$, tak můžeme dostat robustnější definici rozkladu na souvislé komponenty, která nám umožňuje s nimi lépe pracovat za pomocí kongruencí. První iterace vlastně odpovídá rozkladu na orbity pod působením $\Inn{Q}$.

:::definice
Buď $Q$ quandle. Pak definujeme $\Orb[0]{Q} = 1_Q$ Dále definujme $\Orb[n+1]{Q} = \Orb{\Dis{\Orb[n]{Q}}}$.
:::

Cílem je ukázat, že pokud $\Orb[n]{Q} = 0_Q$, tedy se dostaneme do stavu jako na obrázku \ref{rozklado}, pak je $Q$ reduktivní a naopak. Abychom mohli využít síly výše definované konstrukce, potřebujeme nejprve technické lemma.

![Rozklad quandlu na komponenty](../img/rozklad.pdf){#rozklado}

:::{.lemma #blivajz}
Buď $Q$ quandle a $\alpha \in \Con{Q}$. Pak platí, že

$$\Orb[n]{\faktor{Q}{\alpha}} = \{ [b]_{\alpha}: b\: \Orb[n]{Q}\: a\}.$$
:::

:::proof
Tvrzení dokážeme indukcí podle $n$. Pro $n = 0$ je tvrzení triviální, protože vlastně jen popisuje úvodní definici.

Dále budeme předpokládat, že tvrzení platí pro $n$. Tedy:

$$\{ [b]_{\alpha}: [b]_{\alpha}\: \Orb[n]{\faktor{Q}{\alpha}}\: [a]_{\alpha} \} = \{ [b]_{\alpha}: b\: \Orb[n]{Q}\: a \}.$$

Nyní vezměme přirozenou projekci $\pi_{\alpha}: \Inn{Q} \twoheadrightarrow \Inn{\faktor{Q}{\alpha}}$ definovanou jako $\pi_{\alpha}(L_a) = L_{[a]_{\alpha}}$. Pak platí, že $\pi_{\alpha}(\Dis{\Orb[n]{Q}}) = \Dis{\Orb[n]{\faktor{Q}{\alpha}}}$, jelikož grupa na pravé straně je generována prvky tvaru $L_{[a]_{\alpha}} L_{[b]_{\alpha}}^{-1}$, kde $[a]_{\alpha}\: \Orb[n]{\faktor{Q}{\alpha}}\: [b]_{\alpha}$. Jenže $L_{[a]_{\alpha}} L_{[b]_{\alpha}}^{-1} = \pi_{\alpha}(L_a) \pi_{\alpha}(L_b)^{-1} = \pi_{\alpha}(L_a L_b^{-1})$. To jsou ale generátory grupy $\Dis{\Orb[n]{Q}}$, protože $b\: \Orb[n]{Q}\: a$.

Zafixujme si prvek $A = [a]_{\Orb[n+1]{\faktor{Q}{\alpha}}} = \{d([a]_{\alpha}): d \in \Dis{\Orb[n]{\faktor{Q}{\alpha}}} \}$. Z tvrzení výše plyne, že

$$A = \{\pi_{\alpha}(h)([a]_{\alpha}): h \in \Dis{\Orb[n]{\faktor{Q}{\alpha}}}\} = \{[h(a)]_{\alpha}: h \in \Dis{\Orb[n]{Q}}\}.$$

Z toho už ale dostáváme, že:

$$[a]_{\Orb[n+1]{\faktor{Q}{\alpha}}} = \{b_{\alpha}: b\: \Orb[n+1]{Q}\: a\} = \{[b]_{\alpha}: b\: \Orb[n+1]{Q}\: a\},$$

což jsme chtěli dokázat.
:::

:::{.tvrzenic #redbar}
[@bonatto2020quandles].
Buď $Q$ konečný quandle. Pak jsou následující podmínky ekvivalentní:

1) $Q$ je $n$-reduktivní pro nějaké $n \in \N$.

2) $\Orb[n]{Q} = 0_Q$ pro nějaké $n \in \N$.

3) Pro každou komponentu $Q_i$ rozkladu $Q$ platí, že $|Q_i| = 1$.
:::

:::proof
$(1) \implies (2)$:

Dokážeme indukcí podle $n$:

Případ $n = 1$ je triviální, protože se jedná o triviální quandly $T_m$ a tudíž $\Orb[1]{Q} = 0_Q$.

Dále buď $Q$ $n+1$-reduktivní. Zadefinujme homomorfismus $L: Q \rightarrow Q$ tak, že $L: x \mapsto L_x$. Tím dostaneme faktorquandle definovaný jako $\faktor{Q}{\lambda} = L(Q)$, který je ale $n$-reduktivní. Podle indukčního předpokladu tedy platí, že $\Orb[n]{\faktor{Q}{\lambda}} = 0_{\faktor{Q}{\lambda}}$. Z lemmatu \ref{blivajz} pak plyne, že $\{[b]_{\lambda}: b\: \Orb[n]{Q}\: a\} = [[a]_{\lambda}]_{\Orb[n]{\faktor{Q}{\lambda}}} = \{[a]_{\lambda}\}$. Tedy pokud $b\: \Orb[n]{Q}\: a$, tak $[b]_{\lambda} = [a]_{\lambda}$ a tudíž i $b = a$. Tedy $\Orb[n]{Q} \subseteq \lambda$ a tudíž $\Dis{\Orb[n]{Q}} \leq \Dis{\lambda}$. Z toho plyne, že $\Orb[n+1]{Q} = \Orb{\Dis{\Orb[n]{Q}}} \subseteq \Orb{\Dis{\lambda}} = 0_Q$. Tedy $\Orb[n+1]{Q} = 0_Q$.

$(2) \implies (1)$:

Také dokážeme indukcí podle $n$:

Případ $n = 1$ je triviální ze stejného důvodu jako výše.

Dále předpokládejme, že $\Orb[n+1]{Q} = 0_Q$. Definujme $Q' = \faktor{Q}{\Orb[n]{Q}}$. Přirozená projekce $\pi_{\Orb[n]{Q}}$ posílá $\Dis{\Orb[k]{Q}}$ na $\Dis{\faktor{\Orb[k]{Q}}{\Orb[n]{Q}}}$ a podle lemmatu \ref{blivajz} platí, že $\Orb[k]{Q'} = \faktor{\Orb[k]{Q}}{\Orb[n]{Q}}$ pro každé $k \leq n$. Tudíž $Q'$ má řetěz kongruencí:

$$1_{Q'} = \Orb[0]{Q'} \subseteq \Orb[1]{Q'} \subseteq \dots \subseteq \Orb[n]{Q'} = \faktor{\Orb[n]{Q}}{\Orb[n]{Q}} = 0_{Q'}.$$

Z indukce víme, že $Q'$ je $n$-reduktivní. Jelikož $\Orb[n+1]{Q} = 0_Q$, pak orbity $\Dis{\Orb[n]{Q}}$ jsou triviální. Tedy $\Dis{\Orb[n]{Q}} \subseteq \lambda$. Reduktivitu si můžeme reformulovat tak, že platí:

$$((\dots(a * c_1) \dots) * c_{n-1}) * c_n \lambda = ((\dots(b * c_1)\dots) * c_{n-1}) * c_n \lambda.$$

Z toho ale plyne, že $Q$ je $n+1$-reduktivní.

$(2) \implies (3)$:

Vidíme, že $\Orb[n]{Q}$ odpovídá tomu, že budeme postupně rozkládat $Q$ na menší a menší orbity, až dosáhneme rozkladu na souvislé komponenty. Jelikož $\Orb[n]{Q} = 0_Q$, tak všechny komponenty mají velikost $1$.

$(3) \implies (2)$:

Pokud všechny komponenty rozkladu mají velikost $1$, tak to znamená, že existuje $n \leq |Q|$ takové, že $\Orb[n]{Q} = 0_Q$, protože $Q$ je konečný quandle.
:::

:::{.dusledek #redsou}
Jediný souvislý reduktivní quandle je $T_1$.
:::

:::proof
Mějme souvislý reduktivní quandle $Q$. Jelikož je reduktivní, tak podle \ref{redbar} všechny komponenty rozkladu mají velikost $1$. Jenže zároveň je $Q$ souvislý. Tudíž se jedná o $T_1$.
:::

## Barvení pomocí souvislých quandlů

V předchozí kapitole jsme si ukázali, že homomorfním obrazem fundamentálního quandlu je souvislý quandle. Nyní naopak ukážeme, že pro každý netriviální souvislý quandle existuje takový uzel, který má netriviální obarvení. Na základě toho ukážeme, že quandle dává triviální obarvení pro všechny uzly, právě tehdy když je reduktivní.

:::{.veta #stuha}
Pro každý souvislý quandle $Q$, $|Q| > 1$ existuje takový uzel $K$, že $\Col{Q}{K} > 0$.
:::

:::proof
Pro důkaz této věty použijeme konstrukci, která se poprvé objevila v článku [@johnson1980homomorphs], a kterou si upravíme tak, aby řešila náš problém. Konstrukce je následující:

Nejprve uvažujme orientovaný $m$-link, kde $m = |Q|$, viz obrázek \ref{link}. Každou komponentu obarvíme jiným prvkem z $Q$. Následně budeme postupně propojovat pomocí pásků tak dlouho, dokud nám nevznikne uzel. Na konci dostaneme uzel, který bude mít netriviální obarvení, jelikož každá komponenta bude obarvena jiným prvkem z $Q$ a toto obarvení se v průběhu konstrukce zachovává. Z toho pak bude plynout, že $\Col{Q}{K} > 0$.

![$m$-link](../img/link.pdf){#link}

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

Počet komponent je konečný a jednou iterací algoritmu jsme snížili počet komponent o jedna. Algoritmus budeme tedy opakovat tak dlouho, dokud nedostaneme uzel. Takový uzel nazývá *stuhový uzel* (anglicky *ribbon knot*). Jelikož jsme každou komponentu $|Q|$-linku obarvili jiným prvkem z $Q$ a algoritmus toto obarvení zachovává, dostaneme uzel, který bude mít netriviální obarvení. Tedy $\Col{Q}{K} > 0$.
:::

:::priklad
Nyní provedeme konstrukci pro Foxův quandle $F$. Víme, že $2 * 1 = 3$ a $1 * 2 = 3$. Nejprve propojíme komponenty $1$ a $3$, následně připojíme zbývající komponentu $2$ a dostaneme stuhový uzel $R_F$ jako na obrázku \ref{ribfox}.
:::

![Stuhový uzel pro Foxův quandle](../img/ribfox.pdf){#ribfox}

## Barvení pomocí reduktivních quandlů

Nyní už přistoupíme k samotnému důkazu ekvivalence prvních svou tvrzení z věty \ref{hlavni}.

:::{.veta #valoun}
Mějme konečný quandle $Q$. Pak platí jsou následující tvrzení ekvivalentní:

1) $\Col{Q}{K}$ je konstantní,

2) $Q$ je reduktivní.
:::

:::proof
Pokud je $Q$ souvislý a netriviální, pak podle věty \ref{stuha} zkonstruujeme příslušný stuhový uzel $R$ tak, že bude mít netriviální obarvení $\Col{Q}{R} > 0$. Zároveň lze unknot $U$ obarvit pouze triviálně, tedy $\Col{Q}{U} = 0$. Tedy $\Col{Q}{K}$ není konstantní.

$(1) \implies (2)$:

Tuto implikaci ukážeme obměnou. Předpokládáme, že $Q$ není reduktivní. $Q$ podle věty \ref{rozklad} rozkládá na komponenty $(Q_1, Q_2, \dots, Q_n)$. Jelikož $Q$ není reduktivní, pak z \ref{redbar} víme, že existuje komponenta $Q_i$ taková, že $|Q_i| > 1$. Označme si $Q_i$ jako $W$.
Pak podle \ref{stuha} platí, že $\Col{W}{K} > 0$. Jelikož $W \preccurlyeq Q$, tak podle lemmatu \ref{suma} platí, že $\Col{Q}{K} \geq \Col{W}{K} > 0$. A tedy není konstantní.

$(2) \implies (1)$:

Jestliže $Q$ je reduktivní, pak z věty \ref{redbar} platí, že všechny komponenty jsou izomorfní $T_1$. Z věty \ref{hom} plyne, že $\Col{Q}{K} = 0$, a tudíž $\Col{Q}{K}$ je konstantní pro všechny uzly $K$.
:::