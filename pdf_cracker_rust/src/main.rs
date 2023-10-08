/*
    Implémentation en Rust
    ======================
    voilà ça c'est pas un language imprévisible
        -> lecture des bytes sans problème
        -> pas ralenti par le garbage collector
        -> pas de problème de type
        -> pas de problème de compilation
        -> merci le mec qui a invneité le rust en fait
*/

use std::fs::File as FsFile;
use std::io::{BufRead, BufReader};
use std::env;
use std::time::Instant;

use pdf;

fn try_password(pdf_contents: &[u8], password: &str) -> bool {
    pdf::file::FileOptions::cached()
        .password(password.as_bytes())
        .load(pdf_contents)
        .is_ok()
}


fn main() {

    println!("usage:\n\tcargo run <wordlist> <pdffile>");

    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    println!("reading: {}", filename);
    let mut lines = Vec::new();

    if let Ok(file) = FsFile::open(filename) {
        // petit timer pour mesurer le temps d'exécution
        let start_time = Instant::now();

        // Créer un BufReader pour faciliter la lecture ligne par ligne
        let reader = BufReader::new(file);

        // Parcourir chaque ligne du fichier
        for line in reader.lines() {
            if let Ok(line_content) = line {
                lines.push(line_content);
            }
        }
        let elapsed_time = start_time.elapsed();

        println!("{} words loaded in {}.{} seconds", lines.len(), elapsed_time.as_secs(), elapsed_time.subsec_millis());
    } else {
        println!("ERROR: can't read file.");
    }

    println!("now loading: {}", args[2]);
    // Ouvrir le fichier en écriture
    let pdf_bytes = std::fs::read(&args[2]).expect("Unable to read PDF");

    println!("starting bruteforce.");
    let start_time = Instant::now();

    for potential_password in lines {;
        if try_password(&pdf_bytes, &potential_password) {
            let elapsed_time = start_time.elapsed();
            println!("password found in {}.{} seconds: {}", elapsed_time.as_secs(), elapsed_time.subsec_millis(), &potential_password);
            break;
        }
    }


    
}
