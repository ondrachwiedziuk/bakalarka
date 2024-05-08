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
# Úvod {-}

Teorie uzlů je oblast topologie, která se zabývá uzly, což jsou jednoduché uzavřené křivky v trojrozměrném prostoru. Uzly samotné se v historii vyskytují v různých kulturách již od pravěku, ale teorie uzlů jako matematická disciplína vznikla až v 18. století. Mezi slavné matematiky, kteří se zasloužili o vznik a rozvoj této disciplíny, patří například C. F. Gauss (1777-1855), J. W. Alexander (1888-1971) nebo H. Seifert (1907-1996). Velký rozvoj nastal po druhé světové válce ve Spojených státech a Japonsku.

Mezi základní otázky patří, zda jsou dva uzly ekvivalentní, tedy zda je jeden z druhého možné získat spojitou deformací, aniž by se v nějakém okamžiku křivka protínala. Dlouho nebylo známé, jestli vůbec existuje algoritmus, který by dokázal rozhodnout, zda dva zadané uzly jsou ekvivalentní. Existence algoritmu byla prokázaná článku [@Haken1962].
Následně bylo v článku [@Hass1998] dokázáno, že jenom rozhodnutí, zda je uzel triviální, patří do kategorie NP. Na jejich práci bylo navázáno v článku [@Kuperberg2014], kde byla dokázána komplementární vlastnost, že daný problém patří do třídy co-NP.

Základní technikou rozlišování uzlů je hledání invariantů. Mezi nejznámější invarianty patří takzvané barvení uzlů. Z počátku se jednalo např. o Foxovo barvení [@Fox1963], kdy je každý oblouk uzlového diagramu obarven jednou ze tří barev a platí, že na každém křížení se vyskytují všechny tři barvy, nebo je monochromatické. Tato technika se následně zobecnila na barvení pomocí quandlů.

Quandle je algebraická struktura, která vznikla přesně pro účely rozlišování uzlů. Takzvaný fundamentální quandle dokonce jednoznačně určuje uzly až na orientaci a překlopení, což dokázal D. Joyce v článku [@Joyce1982ACI]. Bohužel, výpočet fundamentálního quandle je příliš složitý pro praktické použití. Jako zjednodušení se počítá počet homomorfismů do konečného quandlu. Tomu pak říkáme barvení pomocí quandlu. Obvykle však neuvažujeme triviální barvení, kdy je daný homomorfismus konstantní. Tudíž $\Col{Q}{K} = |\Hom{Q_K}{Q}| - |Q|$, kde $Q_K$ je fundamentální quandle uzlu $K$.

<!-- Odsud dál to chce přepsat, abych vypíchl hlavní větu. -->

#### Charakterizace quandlů s triviálním barvením {-}

V této práci se zaměříme na charakterizaci quandlů, které dávají triviální obarvení pro všechny uzly. Hlavním výsledkem je následující věta:

:::{.veta #hlavni}
Buď $Q$ konečný quandle. Pak jsou následující tvrzení ekvivalentní:

1) $\Col{Q}{K} = 0$ pro všechny uzly $K \in \mathcal{K}$.

2) $\Col{Q}{K}$ je Vassilievův invariant.

3) $Q$ je reduktivní.
:::

Výsledek je zajímavý především z hlediska toho, že zatímco $(1)$ a $(2)$ jsou tvrzení související především s teorií uzlů, tvrzení $(3)$ je čistě algebraické, které vychází z teorie komutátorů pro quandly a s barvením uzlů nemá na první pohled nic společného. Dále pak $(1) \implies (2)$ je zřejmá implikace, tak $(2) \implies (1)$ využívá jako prostředníka tvrzení $(3)$.

V první kapitole jsou definovány základní pojmy z teorie uzlů a quandlů. Ve druhé kapitole definujeme reduktivitu a ukážeme $(1) \iff (3)$. Ve třetí kapitole se zaměříme na Vassilievovy invarianty a ukážeme $(2) \iff (3)$. Také je zde dokázáno obdobné tvrzení pro linky, kde je barvení pomocí quandlů Vassilievův invariant právě tehdy, když je quandle triviální. 

<!-- V této práci se zaměřím na charakterizaci quandlů, které dávají triviální obarvení pro všechny uzly.
V první kapitole jsou definovány základní pojmy z teorie uzlů. Jedná se o víceméně neformální úvod do problematiky uzlů a sám o sobě neobsahuje žádné nové výsledky.
Ve druhé kapitole se budu věnovat quandlům a jejich vlastnostem. Zaměřím se především na spojitost a dokážu pár základních tvrzení o rozkladu quandlu na spojité komponenty.
Ve třetí kapitole zavedu pojem reduktivnosti quandlu a ukážu, že barvení quandlem je pro všechny uzly triviální, právě tehdy když je quandle reduktivní.
Na závěr ve čtvrté kapitole se zaměřím na koncept Vassilievových invariantů a dokážu, že barvení pomocí quandlů je Vassilievův invariant právě tehdy, když je quandle reduktivní. Také rozvinu výsledek z uzlů na linky a ukážu, že barvení pomocí quandlů je Vassilievův invariant pro linky, právě tehdy když je quandle triviální. -->

Tato práce vychází především ze tří článků: [@johnson1980homomorphs], [@eisermann1999number] a [@bonatto2020quandles]. Využijeme podobné důkazové techniky, abychom dosáhli výše uvedeného výsledku. Zatímco [@johnson1980homomorphs] a [@eisermann1999number] se zabývají fundamentálními grupami uzlů, v této práci se obdobná tvrzení formulují pro quandly. Naopak [@bonatto2020quandles] se zabývá reduktivitou quandlů, ovšem nezabývá se vztahem reduktivity a barvení uzlů. Tudíž formulace a důkaz věty \ref{hlavni} je novým výsledkem.
