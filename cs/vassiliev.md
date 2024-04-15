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
# Barvení jako Vassilievův invariant

V této kapitole ukážu další charakterizaci reduktivních quandlů a to pomocí Vassilievových invariantů. Nejprve je ovšem uvést několik základních výsledků z teorie copánkových grup, které následně budou aplikovány v příslušném důkazu.

## Copánky

Copánkovou grupu jako první zavedl Emil Artin v roce 1925. Copánky se skládají z $n$ pramenů, které jsou upevněny k horní a dolní desce a mohou se mezi sebou křížit ve smyslu Reidemeistrových pohybů 2 a 3. My si zavedeme copánkovou grupu pomocí prezentace.

:::definice
Buď zadané číslo $n$. Pak $B_n$ značí grupu danou prezentací $B_n = \langle \sigma_1, \sigma_2, \dots, \sigma_{n-1} |\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}; \sigma_i \sigma_j = \sigma_j \sigma_i \rangle$, kde v první sadě relací $i \in \{1, 2,\dots n-1\}$ a ve druhé $i, j \in \{ 1, 2, \dots, n \}; |i - j| \geq 2$.
:::

První relace je ekvivalentem Reidemeistrova pohybu 3 a druhá relace říká, že pokud jsou příslušné prameny disjunktní, tak se mohou prohazovat.

Skládání $a \cdot b$ funguje geometricky tak, že se vezme spodní deska z $a$ a přilepí se k horní desce $b$ tak, aby na sebe navazovaly příslušné prameny, a pak se prostřední deska odstraní. Jednotkový prvek je copánek bez křížení. Inverzní prvek je symetrické překlopení copánku. Vlastně tak odpovídá Reidemeistrovu pohybu 2.

![Příklad copánku](../img/braid.pdf)

Pokud vezmeme nějaký copánek $b \in B_n$, pak můžeme udělat tzv. *uzávěr*, kdy dojde ke slepení horní a spodní desky tak, že se přilepí k sobě protilehlé prameny. Tímto obecně dostaneme link. Budeme ho značit $K_b$.

![Lepení copánku](../img/glue.pdf)

Jedna z nejznámějších vět z teorie uzlů je Alexanderova věta, která říká, že každý uzel lze získat jako uzávěr nějakého copánku.

:::{.veta #alexander}
(Alexanderova věta).
Pro každý uzel $K$ existuje číslo $n \in \N$ a copánek $b \in B_n$, že $K$ je ekvivalentní uzávěru $K_b$.
:::

Předchozí větu lze použít k definici nového invariantu, a to copánkového indexu. Tento index nám říká, kolik pramenů potřebujeme, abychom mohli dostat daný uzel jako uzávěr copánku s daným počtem pramenů.

:::definice
Pro daný uzel $K$ rozumíme *copánkovým indexem* $s(K)$ (anglicky *braid index*) nejmenší číslo $n$ takové, že existuje $b \in B_n$ tak, aby $K$ byl ekvivalentní uzávěru $K_b$.
:::

:::pozorovani
Copánkové číslo $s(K)$ je invariant.
:::

## Vassilievův invariant

Myšlenka Vassilievových invariantů stojí na zobecnění uzlů na tzv. singulární uzly. Tyto uzly se vyznačují tím, že dovolujeme křivce, aby se protínala samu sebe. V této kapitole vycházíme z knížky [@chmutov2011introduction].

:::definice
*Singulárním bodem* rozumíme bod, kde se křivka protíná sama sebe právě 2 částmi křivky. *Singulárním uzlem* $K^\bullet$ rozumíme uzel, který obsahuje alespoň jeden singulární bod.
:::

![Singulární uzel s 1 singulárním bodem](../img/singular.pdf)

Vassilievové invarianty se zavádí pomocí skein relace. Myšlenka je založena na tom, že invariant pro klasické uzly můžeme rozšířit na třídu singulárních uzlů. Dělá se to pomocí skein relace, kdy si zafixujeme singulární bod pro $K^\bullet$ a lokálně ho nahradíme kladným ($K^+$), resp. negativním ($K^-$) křížením. Následně získáme hodnotu invariantu $v$ pro $K^\bullet$ pomocí hodnot invariantů pro $K^+$ a $K^-$:

$$v(K^{\bullet}) = v(K^+) - v(K^-).$$

![Vassilievova skein relace](../img/skein.pdf){#skein}

Tato hodnota je jednoznačně určená, tudíž nám to dává způsob, jak definovat invariant pro singulární uzly. Pokud má uzel $K^\bullet$ singulární bodů více, tak se postupujeme induktivně, očíslujeme jednotlivé singulární body a dostaneme tak *úplnou rezoluci*:

$$v(K^\bullet) = \sum_{\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n \in \{+,-\}} (-1)^{|\varepsilon|} v(K^{\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n}),$$

kde $|\varepsilon|$ značí počet záporných znamének v n-tici $(\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n)$ a $K^{\varepsilon_1, \varepsilon_2, \dots, \varepsilon_n}$ značí uzly, které vzniknou nahrazením singulárních bodů křížením s orientací podle příslušného znaménka.

Myšlenka Vassiievových invariantů je, že tento vztah můžeme obrátit a říct, že definujeme invariant $v$ tak, aby od určitého počtu singulárních bodů byl nulový.

:::definice
Invariant $v$ se nazývá *Vassilievův*, nebo také *konečného typu* stupně $\leq m$, pokud platí, že pro každý singulární uzel $K^\bullet$ s počtem protnutí $> m$ platí $v(K^\bullet) = 0$. Řekneme, že je stupně $m$, pokud je stupně $\leq m$, ale není stupně $\leq m-1$.
:::

Spousta známých invariantů jsou Vassilievovy invarianty, nebo se dají na něj převést. Ovšem existují příklady invariantů, které nejsou Vassilievovy. Mezi ně, jak si ukážeme, nepatří třeba copánkový index. Důkaz provedeme pomocí sekvence tzv. *twistů* zmíněných v článcích [@Trapp1994] a [@Dean1994].

:::definice
Buď $K$ uzel, pro který zafixujeme jedno křížení, a $z \in \Z$. Pak *twist* $K_z$ je uzel, který vznikne z $K$ tak, že lokálně nahradíme zafixované křížení křížením s $z$ závity jako na obrázku \ref{twist}.
:::

![Twist uzlu](../img/twist.pdf){#twist}

:::{.vetac #twistseq}
[@Trapp1994]
Buď $\{ K_z : z \in \Z \}$ posloupnost twistů. Pokud je invariant $v: \mathcal{K} \rightarrow \C$ Vassilievův stupně nejvýše $m$, tak platí, že $v(K_z)$ tvoří polynom v $z$ stupně nejvýše $m$.
:::

Nyní využijeme pár lemmat z článku [@eisermann1999number], které nám pomohou ukázat, že copánkový index není Vassilievův invariant.

:::{.dusledek #constvas}
Pokud je invariant $v$ omezený na posloupnost twistů, tak je konstantní.
:::

:::proof
Mějme invariant $v$ Vassilievova stupně nejvýše $m$. Podle věty \ref{twistseq} platí, že $v(K_z)$ tvoří polynom v $z$ stupně nejvýše $m$. Jelikož je $v$ také omezený, tak to znamená, že tento polynom je konstantní. Dále, jelikož je součástí posloupnosti twistů uzly $K_0 = K$ i $K_1$, kde dochází ke změně orientace křížení, tak $v(K) = v(K_0) = v(K_1) = v(K)$. Jelikož jsme schopní změnou orientace křížení dostat unknot, tak $v$ musí být nutně konstatní.
:::

:::{.lemma #braidlim}
Copánkové číslo $s(K)$ je omezené na posloupnost twistů.
:::

:::proof
Mějme uzel $K$ a jeho copánkový index $s(K)$. Pak si vezměme z věty \ref{alexander} copánek $b \in B_{s(K)}$ tak, že $K$ je ekvivalentní uzávěru $K_b$. Nyní si zafixujeme jedno křížení a budeme provádět twisty. Twisty zhora pak tedy dávají horní mez na copánkové číslo $K_z$. Zároveň platí, že $s(K) > 0$. Tedy $s(K)$ je omezené na posloupnost twistů.
:::

:::{.vetac #omezeni}
[@eisermann1999number]
Buď $s(K)$ copánkový index uzlu $K$. Pak pokud invariant $v: \mathcal{K} \rightarrow \mathbb{C}$ splňuje, že $|v(K)| \leq f(s(K))$ pro nějakou funkci $f: \mathbb{N} \rightarrow \mathbb{N}$ a pro všechny uzly $K \in \mathcal{K}$, pak $v$ není Vassilievův invariant, nebo je konstantní.
:::

:::proof
Jelikož je copánkový index omezený na posloupnost twistů dle lemmatu \ref{braidlim} a zároveň dokážeme omezit hodnotu invariantu pomocí funkce $f$, tak podle věty \ref{constvas} je invariant $v$ konstantní, nebo není Vassilievův invariant.
:::

<!-- V článku [@eisermann1999number] se autor zabývá otázkou, zda je počet grupových homomorfismů z fundamentální grupy do zvolené grupy $G$ Vassilievův invariant. Jeho výsledkem je charakterizace, že pokud je $G$ nilponentní, tak je počet homomorfismů konstantní, jinak není Vassilievův invariant. V tété kapitole se pokusíme zobecnit tento výsledek na quandle.

Motivací je, že fundamentální quandle je úplný invariant, tedy plně charakterizuje uzel. Zároveň platí, že grupové homomorfismy mají svojí representaci i jako quandleové homomorfismy, ovšem ne každý quandleový homomorfismus má svojí reprezentaci jako grupový homomorfismus. Tedy pokud bychom dokázali obdobný výsledek pro quandleové homomorfismy, tak bychom mohli získat silnější výsledek, než který je v původním článku. -->

## Barvení uzlů

Nyní využijeme znalosti z předchozí podkapitoly o copánkovém indexu. Zatímco v článku [@eisermann1999number] se autor zabývá grupovými homomorfismy, my jeho výsledek zobecníme na quandlové barvení. Abychom ukázali, že se jedná o obecnější výsledek, tak si všimněme, že foxovo barvení nelze dostat jako $\Conj{G}$ pro nějakou grupu $G$. Pokud ano, tak by grupa $G$ byla velikosti 3, jenže jediná grupa velikosti 3 je cyklická grupa $\Z_3$, která je abelovská. Jenže $\Conj{\Z_3}$ je trivialní quandle $T_{\Z_3}$, což není foxovo barvení. Tedy jsme získali silnější výsledek, než který je v původním článku.

:::{.veta #kukurice}
Pro každý quandle $Q$ platí, že počet obarvení $\Col{Q}{K}$ není Vassilievův invariant, nebo je konstantní.
:::

:::proof
Mějme fixně zadaný quandle $Q$. Uvažujme libovolný uzel $K$ a copánek $b \in B_{s(K)}$, kde $K_b \cong K$. Pak platí, že máme-li konkrétní obarvení $f \in \text{Hom}(Q_K, Q)$, tak je jednoznačně určeno obarvením konců provázků v copánkové reprezentaci. Tedy platí, že $\Col{Q}{K}$ dokážeme omezit tak, že každému konci přiřadíme nějaký prvek z $Q$. Tedy

$$\Col{Q}{K} \leq |Q|^{s(K)}.$$

Použitím věty \ref{omezeni} dostáváme, že $\Col{Q}{K}$ není Vassilievův invariant, nebo je konstantní.
:::

:::dusledek
Mějme quandle $Q$. Pak platí, že není Vassilievův invariant, právě tehdy když není reduktivní.
:::

:::proof
Z věty \ref{valoun} plyne, že $\Col{Q}{K}$ je konstantní, právě tehdy když $Q$ je reduktivní. Z věty \ref{kukurice} plyne, že $\Col{Q}{K}$ je Vassilievův invariant, právě tehdy když je konstantní. Tedy obě tvrzení jsou ekvivalentní.
:::

:::dusledek
Mějme grupu $G$. Pak platí, že následující tvrzení jsou ekvivalentní:

1) $G$ je nilpotentní;

2) quandle $\Conj{G}$ je reduktivní.
:::

:::proof
V článku [@eisermann1999number] bylo obdobným způsobem dokázáno, že grupa $G$ je nilpotentní, právě tehdy když počet homomorfismů z fundamentální grupy uzlu do $G$ je konstantní. Naopak z věty \ref{valoun} plyne, že quandle $\Conj{G}$ je reduktivní, právě tehdy když počet obarvení uzlu quandlem $\Conj{G}$ je konstantní. Z toho plyne ekvivalence pro obě tvrzení.
:::

## Barvení linků

Obdobnou charakterizaci můžeme získat i pro linky. Ovšem, v tomto případě bude vše jednodušší. Nejprve se sluší říct, že musíme změnit definici barvení linku, jelikož pokud budeme uvažovat $m$-link, tak platí, že počet obarvení quandlem $Q$ je rovno $|Q|^m$. Tedy $\Col{Q}{K}$ je konstatní pouze pro $T_1$. To můžeme opravit tím, že nebudeme započítávat obarvení, která jsou triviální. Tedy $\Col[+]{Q}{L} = \Col{Q}{L} - |Q|^l$, kde $l$ je počet komponent linku $L$.

:::veta
Uvažujme quandle $Q$ a link $L$ s alespoň 2 komponentami. Pak platí, že $\Col[+]{Q}{L}$ není Vassilievův invariant, nebo je konstantní. Navíc $\Col[+]{Q}{L}$ je konstantní, právě tehdy když $Q$ je trivialní quandle.
:::

:::proof
První část je jen variací věty \ref{kukurice}, kde místo uzlu uvažujeme link.

Dále, pokud je $Q$ triviální quandle, tak jak platí, že $\Col[+]{Q}{L} = 0$ pro všechny linky $L$. Tedy $\Col{Q}{L}$ je konstantní.

Naopak Uvažujme quandle $Q$, který není triviální. Pak jako $L$ označíme $2$-link a jako $H$ hopf link. 

Pro $L$ platí, že $\Col[+]{Q}{L} = 0$ pro všechny quandly $Q$.

Jelikož $Q$ není trivialní, tak existuje dvojice prvků $a, b \in Q$ taková, že $a \neq b$ a $a * b \neq b$. Pokud obarvíme $H$ tak, že první komponentu obarvíme prvkem $a$ a druhou komponentu obarvíme prvkem $b$, tak ze vztahu výše plyne, že $H$ nejde touto dvojicí prvků obarvit. Tedy $\Col[+]{Q}{L} < 0$ a $\Col{Q}{L}$ není konstantní.
:::
