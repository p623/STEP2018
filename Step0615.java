import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.lang.Integer;

public class Step0615{
    public static void main(String[] args){
        Scanner scanner =new Scanner(System.in);
        System.out.println("調べたい単語を入力してください: ");
        String inputWord= scanner.next();
        //System.out.println("類似性を調べたい単語を入力してください(単語2): ");
        //String inputWord2=scanner.next();
       int inputWordIndex=wikiWordsSearch(inputWord);
       relatedWordsSearch(inputWordIndex);


        // inputWord1_Index = wikiWords_Search(inputWord1)
        // relatedWords1=relatedWords_Search(inputWord1_Index)

        // inputWord2_Index = wikiWords_Search(inputWord2)
        // relatedWords2=relatedWords_Search(inputWord2_Index)

        // relationship = evaluate_Relationship(relatedWords1,relatedWords2)
        // print("--------------------------------------------------")
        // print("類似性は"+str(relationship) +"%です")

    }

    public static ArrayList<String> readWikiWords() {
        ArrayList<String> wikiWords = new ArrayList<String>();
        try{
            Scanner scanner = new Scanner(new File("pages.txt"));
            System.out.println("read File");
            while(scanner.hasNextLine()){
                String pageLine =scanner.nextLine();
                String[] indexWikiWord =pageLine.split("\t");
                wikiWords.add(indexWikiWord[1]);
            }
            System.out.println("finish make wikiWords");
        } catch (FileNotFoundException e){
            System.out.println("can't read File");
            }
        return wikiWords;
        // # wikiWords=['アンパサンド', '言語', '日本語',...]    
    }

    public static int wikiWordsSearch(String inputWord){
        ArrayList<String> wikiWords = readWikiWords();
        // # wikiWords=['アンパサンド', '言語', '日本語',...]
        if(wikiWords.contains(inputWord)){
            System.out.println("--------------------------------------------------");
            System.out.println("'"+inputWord+"'についてのサイトはWikipediaに存在します");
            return wikiWords.indexOf(inputWord);
            // # return index of inputWord -> relatedWords_Search
        }else{
            System.out.println("'"+inputWord+"'についてのサイトはWikipediaに存在しません");
            System.out.println("Error");
            return -1;
        }
    }
     
    public static ArrayList<String> relatedWordsSearch(int inputWordIndex){
        if(inputWordIndex==-1){
            ArrayList<String> nullList =new ArrayList<String>();
            return nullList;
        }else{
            ArrayList<Integer> wordIndexs = new ArrayList<Integer>();
            ArrayList<Integer> wikiLinks = new ArrayList<Integer>();
            ArrayList<String> relatedWords = new ArrayList<String>();
            ArrayList<String> wikiWords = readWikiWords();
            try{
                Scanner scanner = new Scanner(new File("links2.txt"));
                System.out.println("Read File");
                while(scanner.hasNextLine()){
                    String linkLine =scanner.nextLine();
                    String[] wordIndexWikiLink = linkLine.split("\t");
                    wordIndexs.add(Integer.valueOf(wordIndexWikiLink[0]));
                    wikiLinks.add(Integer.valueOf(wordIndexWikiLink[1]));
                    // #wordIndexs=[0,0,0,...]
                    // #WikiLinks=[284171, 955, 591, ...]
                }
                
            }catch(FileNotFoundException e){
                System.out.println("can't read File");
            }
            System.out.println("Finish reading File");
            int paramForWordIndexs = 0;
            while (paramForWordIndexs < wordIndexs.size()) {
                if (wordIndexs.get(paramForWordIndexs) > inputWordIndex) {
                    break;
                } else if (wordIndexs.get(paramForWordIndexs) == inputWordIndex) {
                    relatedWords.add(wikiWords.get(wikiLinks.get(paramForWordIndexs)));
                }
                paramForWordIndexs++;
            }
            System.out.println("--------------------------------------------------");
            System.out.println(wikiWords.get(inputWordIndex)+"のサイトから飛べるリンクの一覧を表示します");
            System.out.println(relatedWords);
            return relatedWords;
        }
    }
        
}

 //def evaluate_Relationship(relatedWords1,relatedWords2):
    //matchedNumber=0
    //matchedWords=[]
    //if relatedWords1=="null" or relatedWords2=="null":
        //pass

    //elif len(relatedWords1) <= len(relatedWords2):
        //for relatedWord1 in relatedWords1:
            //if relatedWord1 in relatedWords2:
                //matchedNumber+=1
                //matchedWords.append(relatedWord1)
        //print("--------------------------------------------------")
        //print("単語1と単語2のサイトの両方から飛べるリンクの一覧を表示します")
        //print("--------------------------------------------------")
        //print(matchedWords)
        //return 100*matchedNumber/len(relatedWords1)
    //else:
        //for relatedWord2 in relatedWords2:
            //if relatedWord2 in relatedWords1:
                //matchedNumber+=1
                //matchedWords.append(relatedWord2)
        //print("--------------------------------------------------")
        //print("単語1と単語2のサイトの両方から飛べるリンクの一覧を表示します")
        //print("--------------------------------------------------")
        //print(matchedWords)
        //return 100*matchedNumber/len(relatedWords2)   
    
 
