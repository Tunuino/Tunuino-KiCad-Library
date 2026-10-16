This folder contains gerEFI libaries. These files are used by KICAD in circuit board layouts. 

As of Jan 2024 KiCad 4.0.7 is the offical KICAD for gerEFI's layouts. 

Please note that you would need to fork https://github.com/gerefi/kicad-libraries if
you would like to contribute to gerEFI component library - you cannot contribute to
this using https://github.com/gerefi/gerefi or other repositories


.lib schematic symbol (still usually multiple symbols in one file)

.kicad_mod PCB footprint in KiCad 4+ format (looks like usually one footprint in one file)

.mod - PCB footprint prior to KiCad 4 (could be multiple footprints in one file)

.net is technically not a true source file since it's produced from .sch schematics but
   InteractiveHtmlBOM likes to use these files as input. Open question how does InteractiveHtmlBOM use these .net files exactly? 
   
   
[HOWTO JLC process](Fabrication/jlc_process.md)   
