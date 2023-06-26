# Variables et constantes
## Variables


Une variable est un identificateur dont la valeur peut être modifiée à l'exécution.


 


La syntaxe de base de la déclaration d'une variable est :


 

```
var
  Variable: type;
```

 


Par exemple :


 

```
var
  I: Integer;
```

 


déclare une variable I de type Integer


 


et :


 

```
var
  X: Double;
```

 


déclare une variable X de type Double.


 


Dans des déclarations de variables consécutives, il n'est pas nécessaire de répéter le mot réservé var :

```
var
  X: Double;
  Y: Double;
  Z: Double;
  I: Integer;
  J: Integer;
  K: Integer;
  S: string;
  OK: Boolean;
```

### Règles de nommage des variables








|   | Exemple d'identificateur incorrect | Exemple d'identificateur correct |
|---|---|---|
| Ne peut commencer par un chiffre | 1nom | nom1 |
| Les points ne sont pas autorisés | nom.2 | nom\_2 |
| Les tirets ne sont pas autorisés | -nom-3 |  \_nom\_3 |
| Les espaces ne sont pas autorisés | Nom de variable | Nom\_de\_variable |
| Les caractères accentués ne sont pas autorisés | deuxième\_choix | deuxieme\_choix |
| Les cédilles ne sont pas autorisées | mot\_français | mot\_francais |


### Assignation de valeur à une variable


Vous pouvez fixer une valeur à une variable à tout moment dans le programme ou à partir d'une autre variable par exemple :


 

```
procedure AssignerVariable;


var


  VariableSource: Integer;


  VariableCible: Integer;


begin


  VariableSource := 'Rambouillet';


  VariableCible := '78120 ' + VariableSource;


end.
```

## Constantes


Les constantes sont proches des variables, à un point près : elles ne peuvent pas changer de valeur au cours du programme.


 


Pour déclarer une constante, il faut les déclarer après le mot réservé const au lieu de var.


 

```
procedure DeclarerConstante;


const


  Constante1 = 12;


var


  Variable1: Integer;


begin


end.
```

