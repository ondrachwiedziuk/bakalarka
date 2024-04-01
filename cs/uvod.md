---
documentclass: report
statement-kinds:
    definice:
        style: definition
    tvrzeni:
        style: definition
---
# Úvod {-}

Teorie uzlů je oblast topologie, která se zabývá uzly, což jsou jednoduché uzavřené křivky v trojrozměrném prostoru. Uzly samotné se v historii vyskytují v různých kulturách již od pravěku, ale teorie uzlů jako matematická disciplína vznikla až v 18. století. Mezi slavné matematiky, kteří se zasloužili o vznik a rozvoj této disciplíny, patří například C. F. Gauss (1777-1855), J. W. Alexander (1888-1971) nebo H. Seifert (1907-1996). Velký rozvoj nastal po druhé světové válce ve Spojených státech a Japonsku.

Mezi základní otázky patří, zda jsou dva uzly ekvivalentní, tedy zda je jeden z druhého možné získat spojitou deformací, aniž by se v nějakém okamžiku křivka protínala. Dlouho nebylo známé, jestli vůbec existuje algoritmus, který by dokázal rozhodnout, zda dva zadané uzly jsou ekvivalentní. Existence algoritmu byla prokázaná Hakenem v roce 1962.
Hass a Lagarias následně v roce 1991 dokázali, že jenom rozhodnutí, zda je uzel triviální, patří do kategorie NP.

Základní technikou rozlišování uzlů je hledání invariantů. Mezi nejznámější invarianty patří takzvané barvení uzlů. Z počátku se jednalo např. o Foxovo barvení, kdy je každý oblouk uzlového diagramu obarven jednou ze tří barev a platí, že na každém křížení se vyskytují všechny tři barvy, nebo je monochromatické. Tato technika se následně zobecnila na barvení pomocí quandlů.

Quandle je algebraická struktura, která vznikla přesně pro účely rozlišování uzlů. Takzvaný fundamentální quandle dokonce jednoznačně určuje uzly až na orientaci a překlopení, což dokázal D. Joyce v roce 1982. Bohužel, výpočet fundamentálního quandle je příliš složitý pro praktické použití. Jako zjednodušení se počítá počet homomorfismů do konečného quandle.

V této práci se zaměřím na charakterizaci quandlů, které dávají triviální obarvení pro všechny uzly. V první kapitole jsou definovány základní pojmy z teorie uzlů. V druhé kapitole provedu charakterizaci těchto quandlů, kdy postupně rozvinu teorii kolem spojitých a reduktivních quandlů a následně ukážu, že quandle dávající triviální obarvení pro všechny uzly jsou právě ty, které jsou reduktivní. Ve třetí kapitole se následně zaměřím na koncept Vassilievových invariantů a dokážu, že barvení pomocí quandlů je Vassilievův invariant právě tehdy, když je quandle reduktivní.

Ve své práci vycházím především ze tří článků: \cite{eisermann1999number}, \cite{johnson1980homomorphs} a \cite{bonatto2020quandles}. Využívám podobné důkazové techniky, abych dosáhl svých výsledků.
