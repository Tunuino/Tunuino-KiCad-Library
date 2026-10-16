# Tunuino KiCad Library

Biblioteca de símbolos, footprints e modelos 3D para os projetos eletrónicos Tunuino.

## Estado da migração

Esta biblioteca foi importada a partir de uma biblioteca KiCad legada e adaptada ao nome Tunuino. A pasta de footprints é `tunuino_lib.pretty`. Os dois footprints de logótipos da rusEFI foram removidos intencionalmente.

**A compatibilidade completa com KiCad 9 ainda não foi validada.** Muitos ficheiros usam formatos antigos de KiCad (`.lib`, `.mod` e `(module ...)`), pelo que podem exigir conversão pelo próprio KiCad. Não assumir que a alteração do README converteu os ficheiros.

## Licenças e proveniência

Parte do conteúdo pode ter autores e licenças de terceiros. O antigo ficheiro informativo `Credit_lic.txt` foi removido do repositório. As licenças incluídas nas ferramentas de fabrico e os avisos legais dos próprios ficheiros devem ser preservados e revistos antes de qualquer relicenciamento.

Origem histórica da biblioteca: `rusefi/kicad-legacy-libraries`, revisão de referência `6f95125ede0cd79ac943646ba923cc5db0515922`. Esta referência é apenas de proveniência e não constitui uma dependência Git.

## Integração

Antes de alterar o submódulo no firmware Tunuino, verificar as referências à pasta `tunuino_lib.pretty`, os modelos 3D, os scripts de fabrico e os formatos de símbolos e footprints.
