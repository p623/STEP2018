import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Integer;
import java.lang.System;
import java.util.Collections;

public class Step0615{
    public static void main(String[] args){
        Scanner scanner =new Scanner(System.in);
        System.out.println("調べたい単語を入力してください:");
        String inputWord= scanner.next();
        

        int inputWordIndex = wikiWordsSearch(inputWord);
        ArrayList<Integer> relatedWordsIndex=relatedWordsSearch(inputWordIndex);
        ArrayList<Integer> reRelatedWords=reRelatedWordsSearch(relatedWordsIndex);
        double percent=reRelatedPerRelated(relatedWordsIndex,reRelatedWords);
        System.out.println("--------------------------------------------------");
        System.out.println(inputWord+"の'友達の友達'に含まれる'友達'の割合は"+ percent+"%です");

    }

    public static String[] readWikiWords() {
        String wikiWords [] = new String[1500000];
        int paramForWikiWords=0;
        try{
            Scanner scanner = new Scanner(new File("pages.txt"));
            System.out.println("open File, 'pages.txt'");
            while(scanner.hasNextLine()){
                String pageLine =scanner.nextLine();
                String[] indexWikiWord =pageLine.split("\t");
                wikiWords[paramForWikiWords]=indexWikiWord[1];
                paramForWikiWords++;
            }
        } catch (FileNotFoundException e){
            System.out.println("can't open File, 'pages.txt'");
            }
        return wikiWords;
        // # wikiWords=['アンパサンド', '言語', '日本語',...]    
    }

    public static int wikiWordsSearch(String inputWord){
        String wikiWords[] = readWikiWords();
        // # wikiWords=['アンパサンド', '言語', '日本語',...]
        if(Arrays.asList(wikiWords).contains(inputWord)){
            System.out.println("--------------------------------------------------");
            System.out.println("'"+inputWord+"'についてのサイトはWikipediaに存在します");
            return Arrays.asList(wikiWords).indexOf(inputWord);
            // # return index of inputWord -> relatedWords_Search
        }else{
            System.out.println("'"+inputWord+"'についてのサイトはWikipediaに存在しません");
            System.out.println("Error");
            return -1;
        }
    }
     
    public static ArrayList<Integer> relatedWordsSearch(int inputWordIndex){
        if(inputWordIndex==-1){
            ArrayList<Integer> nullList = new ArrayList<Integer>(1);
            return nullList;
        }else{
            int wordIndexs[] = new int[60000000];
            int wikiLinks[] = new int[60000000];
            ArrayList<String> relatedWords = new ArrayList<String>(150000);
            ArrayList<Integer> relatedWordsIndex = new ArrayList<Integer>(150000);
            String[] wikiWords = readWikiWords();
            try{
                Scanner scanner = new Scanner(new File("links.txt"));
                System.out.println("open File, 'links.txt'");
                int paramForWikiLinks=0;
                while(scanner.hasNextLine()){
                    //long before = System.nanoTime();
                    String linkLine =scanner.nextLine();
                    String[] wordIndexWikiLink = linkLine.split("\t");
                    wordIndexs[paramForWikiLinks]=Integer.valueOf(wordIndexWikiLink[0]);
                    wikiLinks[paramForWikiLinks]=Integer.valueOf(wordIndexWikiLink[1]);
                    paramForWikiLinks++;
                    //long after = System.nanoTime();
                    //System.out.println((after - before));
                    // #wordIndexs=[0,0,0,...]
                    // #WikiLinks=[284171, 955, 591, ...]
                }
                
            }catch(FileNotFoundException e){
                System.out.println("can't read File, 'links.txt'");
            }
            int paramForWordIndexs = 0;
            int paramForRelatedWordsIndex=0;
            while (paramForWordIndexs < wordIndexs.length) {
                if (wordIndexs[paramForWordIndexs] > inputWordIndex) {
                    break;
                } else if (wordIndexs[paramForWordIndexs] == inputWordIndex) {
                    relatedWords.add(Arrays.asList(wikiWords).get(wikiLinks[paramForWordIndexs]));
                    relatedWordsIndex.add(wikiLinks[paramForWordIndexs]);
                    paramForRelatedWordsIndex++;
                }
                paramForWordIndexs++;
            }
            System.out.println("--------------------------------------------------");
            System.out.println(Arrays.asList(wikiWords).get(inputWordIndex) + "のサイトから飛べるリンクの一覧を表示します");
            System.out.println(Arrays.asList(relatedWords));
            Collections.sort(relatedWordsIndex);
            return relatedWordsIndex;
        }
    
    }

    public static ArrayList<Integer> reRelatedWordsSearch(ArrayList<Integer> relatedWordsIndex) {
        //for relatedWordIndex in relatedWordsIndex; 
            ArrayList<Integer> reRelatedWords = new ArrayList<Integer>(30000000);   
            int wordIndexs[] = new int[60000000];
            int wikiLinks[] = new int[60000000];
            String[] wikiWords = readWikiWords();
            try {
                Scanner scanner = new Scanner(new File("links.txt"));
                System.out.println("open File, 'links.txt'");
                int paramForWikiLinks = 0;
                while (scanner.hasNextLine()) {
                    // long before = System.nanoTime();
                    String linkLine = scanner.nextLine();
                    String[] wordIndexWikiLink = linkLine.split("\t");
                    wordIndexs[paramForWikiLinks] = Integer.valueOf(wordIndexWikiLink[0]);
                    wikiLinks[paramForWikiLinks] = Integer.valueOf(wordIndexWikiLink[1]);
                    paramForWikiLinks++;
                    // long after = System.nanoTime();
                    // System.out.println((after - before));
                    // #wordIndexs=[0,0,0,...]
                    // #WikiLinks=[284171, 955, 591, ...]
                }

            } catch (FileNotFoundException e) {
                System.out.println("can't read File, 'links.txt'");
            }
            System.out.println("Finish reading File, 'links.txt'");
            //ここの中身確認する！
                for (int paramForReRelatedWords = 0; paramForReRelatedWords < relatedWordsIndex.size(); paramForReRelatedWords++) {
                    for(int paramForReRelatedWordsSearch=0; paramForReRelatedWordsSearch<wordIndexs.length;paramForReRelatedWordsSearch++){
                        if(wordIndexs[paramForReRelatedWordsSearch]==relatedWordsIndex.get(paramForReRelatedWords)){
                            if(!(reRelatedWords.contains(wikiLinks[paramForReRelatedWordsSearch]))){
                                reRelatedWords.add(wikiLinks[paramForReRelatedWordsSearch]);
                            }
                        }else if(wordIndexs[paramForReRelatedWordsSearch]> relatedWordsIndex.get(relatedWordsIndex.size()-1)){
                            break;
                        }
                    }
            }
        Collections.sort(reRelatedWords);
        return   reRelatedWords;
        
            
    }

    public static double reRelatedPerRelated( ArrayList<Integer> relatedWordsIndex, ArrayList<Integer> reRelatedWords ){
        int matchedCount=0;
        for(int paramForCalPer=0;paramForCalPer< relatedWordsIndex.size();paramForCalPer++){
            if(reRelatedWords.contains(relatedWordsIndex.get(paramForCalPer))){
                matchedCount++;
            }
        }
        return (double)matchedCount*100/ reRelatedWords.size();
    }


}

 