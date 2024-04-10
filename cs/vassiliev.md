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
# Barvení jako Vassilievův invariant

## Copánky

Jedním z užitečných pohledů na uzly je přes takzvané copánky. Něco o historii.

:::definice
Buď zadané číslo $n$. Pak $B_n$ značí grupu danou prezentací $B_n = \langle \sigma_1, \sigma_2, \dots, \sigma_{n-1} |\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}; \sigma_i \sigma_j = \sigma_j \sigma_i \rangle$, kde $i, j \in \{ 1, 2, \dots, n - 1 \}; |i - j| \geq 2$.
:::

Copánky si můžeme představit jako $n$ šňůrek natažených mezi dvěma deskami, přičemž pro ně platí Reidemeisterovy pohyby 2 a 3. Skládání $a \cdot b$ funguje tak, že se vezme spodní deska z $a$ a přilepí se k horní desce $b$ tak, aby na sebe navazovaly provázky, a pak se ty desky odstraní, aby byly opět jenom horní a dolní. Prvky $b$ tedy budeme ztotožňovat s příslušnou geometrickou konstrukcí. 

![Příklad copánku](../img/braid.pdf)

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

## Vassilievův invariant

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

Použitím věty \ref{omezeni} dostáváme, že $\Col{Q}{K}$ není Vassilievův invariant, nebo je konstantní.
:::

:::dusledek
Mějme quandle $Q$. Pak platí, že není Vassilievův invariant, právě tehdy když není reduktivní.
:::

:::proof
Z věty \ref{valoun} plyne, že $\Col{Q}{K}$ není konstantní, právě tehdy když $Q$ není reduktivní. Z věty \ref{kukurice} plyne, že $\Col{Q}{K}$ není Vassilievův invariant, právě tehdy když není konstantní. Tedy obě tvrzení jsou ekvivalentní.
:::

:::dusledek
Mějme grupu $G$. Pak platí, že následující tvrzení jsou ekvivalentní:

1) $G$ je nilpotentní;

2) quandle $\Conj{G}$ je reduktivní.
:::

:::proof
V článku [@eisermann1999number] bylo obdobným způsobem dokázáno, že grupa $G$ je nilpotentní, právě tehdy když počet homomorfismů z fundamentální grupy uzlu do $G$ je konstantní. Naopak z věty \ref{valoun} plyne, že quandle $\Conj{G}$ je reduktivní, právě tehdy když počet obarvení uzlu quandlem $\Conj{G}$ je konstantní. Tedy obě tvrzení jsou ekvivalentní.
:::

## Barvení linků

Obdobnou charakterizaci můžeme získat i pro linky. Ovšem, v tomto případě bude vše jednodušší.

:::veta
Uvažujme quandle $Q$ a link $L$ s alespoň 2 komponentami. Pak platí, že $\text{Col}_Q(L)$ není Vassilievův invariant, nebo je konstantní. Navíc $\text{Col}_Q(L)$ je konstantní, právě tehdy když $Q$ je trivialní quandle.
:::

:::proof
První část je jen variací věty \ref{kukurice}, kde místo uzlu uvažujeme link.

Dále, pokud je $Q$ triviální quandle, tak jak platí, že $\text{Col}_Q(L) = |Q|^l$, kde $l$ je počet komponent linku $L$. Tedy $\text{Col}_Q(L)$ je konstantní pro všechny linky $L$ s $l$ komponentami.

Naopak Uvažujme quandle $Q$, který není triviální. Pak jako $L$ označíme $2$-link a jako $H$ hopf link. 

Pro $L$ platí, že $\text{Col}_Q(L) = |Q|^2$ pro všechny quandly $Q$.

Jelikož $Q$ není trivialní, tak existuje dvojice prvků $a, b \in Q$ taková, že $a \neq b$ a $a * b \neq b$. Pokud obarvíme $H$ tak, že první komponentu obarvíme prvkem $a$ a druhou komponentu obarvíme prvkem $b$, tak ze vztahu výše plyne, že $H$ nejde touto dvojicí prvků obarvit. Tedy $\text{Col}_Q(H) < |Q|^2$. Tedy $\text{Col}_Q$ není konstantní.
:::
