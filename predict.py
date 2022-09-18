from transformers import TextClassificationPipeline
from transformers import BertTokenizer, BertForSequenceClassification
import torch 
from torch import nn


model = BertForSequenceClassification.from_pretrained("model", num_labels=3)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#label: 0 0 2 0 2
raw_input = ["Besides his most recent trip to Quetta , Mr. Rahami visited Karachi , Pakistan , in 2005 . Both of those cities \u2019 reputations have become entwined with the militant groups who have sheltered there : Karachi as a haven for the Pakistani Taliban and Al Qaeda , and Quetta as the headquarters of the exiled Afghan Taliban leadership . But both cities are also home to generations of Afghans who have fled violence in their home country .\nMuch about his New Jersey life did seem unremarkable . Amarjit Singh , a limousine driver , was friends with Mr. Rahami at Edison High School . The person he knew , he said , was a determined student with an abundance of friends and a string of girlfriends . \u201c Everyone seemed to like him , \u201d he said . \u201c Smart , funny , humble . \u201d\nHe viewed the teenage Mr. Rahami as the prototypical immigrant , teetering between two worlds . While he wore jeans and sweatshirts like his friends and worked at a Pathmark supermarket after school , he preferred Afghan music and prayed at the mosque on Friday . Collisions between those worlds sometimes led to rifts with his father , who was more religious and traditional . \u201c The two of them would argue , \u201d Mr. Singh said . \u201c There seemed to be a lot of tension . \u201d\nHis father was especially displeased when Mr. Rahami had a daughter with a high school girlfriend , according to friends . Reached at her home on Monday night , she declined to comment . \u201c My heart is just broken , \u201d said the woman , who The New York Times is not identifying . \u201c I don \u2019 t even know what to think . \u201d\nAfter high school , Mr. Singh said that he and Mr. Rahami had worked together for a while on the night shift at Royal Fried Chicken in Newark . Mr. Singh worked the fryer in the back . Mr. Rahami handled the register . Whenever Mr. Singh got into a dispute with customers , he remembered Mr. Rahami stepping in as the peacemaker . In recent years , the two drifted apart . Mr. Singh was also aware that Mr. Rahami had traveled abroad and that he had become more religious and had taken to wearing Muslim robes .\nThe events on Monday were not Mr. Rahami \u2019 s first encounter with law enforcement . He was arrested in 2014 on weapons and aggravated assault charges for allegedly stabbing a relative in the leg in a domestic incident , according to court documents . He spent over three months in jail on the charges , according to a high-ranking law enforcement official with knowledge of the investigation . A grand jury , however , declined to indict Mr. Rahami . He also spent a day in jail in February 2012 for allegedly violating a restraining order , the official said .",
             "Poll : Prestigious Colleges Wo n't Make You Happier In Life Or Work\nThere 's plenty of anxiety in the U.S. over getting into a top college . But a new Gallup poll suggests that , later in life , it does n't matter nearly as much as we think . In fact , when you ask college graduates whether they 're `` engaged '' with their work or `` thriving '' in all aspects of their lives , their responses do n't vary one bit whether they went to a prestigious college or not .\nThe surprising findings come in a survey of 29,650 college graduates of all ages by Gallup pollsters working with researchers at Purdue University . The poll asked graduates a range of questions designed to measure how well they are doing in life across factors such as income and `` engagement '' in their jobs and careers .\nThe survey set a high bar . It found that 39 percent of college grads overall say they 're `` engaged '' at work ( which is 10 points higher than the population at large ) . And , while almost 5 in 6 self-report doing great in at least one sphere \u2014 whether sense of purpose , financial security , physical health , close relationships or community pride \u2014 only 11 percent are `` thriving '' in all five areas of well-being .\nThose percentages did not vary based on whether the grads went to a fancy name-brand school or a regional state college , one of the top 100 in the U.S. News & World Report rankings or one of the bottom 100 . A slight edge did go to those who attended campuses with more than 10,000 students , while for-profit college graduates saw worse outcomes .\nNo opinion poll can fully capture the impact \u2014 or allure \u2014 of attending a world-famous institution . But this is n't the first time studies have documented no edge for highly selective schools . Previous studies have shown no link between expensive private colleges and later salary for graduates . Income is much more closely tied to a person 's choice of a major , which is a finding the Gallup survey also supported .\nHigh-end colleges often boast that their long-term results should be judged not by looking at paychecks , but at whether their graduates live lives of meaning and deep satisfaction . `` A college degree should be ... a passport to a lifetime of citizenship , opportunity , growth and change , '' wrote Harvard 's president , Drew Gilpin Faust , in a letter to The New York Times last year .\nWell , this survey asked about all that qualitative stuff \u2014 purpose , motivation to achieve goals , opportunity to learn and grow \u2014 and it did n't find any broad influence whatsoever , whether a person 's diploma cost $ 25,000 or $ 250,000 .\nFor Gallup , `` well-being '' and `` engagement '' are n't squishy . They have very specific meanings . In surveys of 25 million people over a number of years , the researchers have asked similar questions and correlated the responses across populations with income , health , employee turnover , company revenue and other `` hard '' indexes .\nThe graduate survey released Tuesday suggests the factors that should be guiding college decisions are not selectivity or prestige , but cost of attendance , great teaching and deep learning , in that order .\nThat 's because graduates who said they had a `` mentor who encouraged my hopes and dreams , '' `` professors who cared about me '' and at least one prof who `` made me excited about learning '' are three times more likely to be thriving and twice as likely to be engaged at work . In a similar vein , grads who did long-term projects and internships and were heavily into extracurriculars are twice as likely to be engaged in their careers today .\nCollege debt also has a big impact , on the negative side . Only 2 percent of those with $ 20,000 to $ 40,000 in undergraduate loans reported they were `` thriving . '' That 's pretty troubling , since $ 29,400 is the national average for the 7 in 10 students who borrow . \u00ad\nGallup and Purdue hope to use these and future surveys to help colleges better focus on outcomes , and to identify `` outlier '' colleges that are doing a great job delivering quality experiences for an affordable price .\nIn the meantime , the take-home message for students is clear , says Brandon Busteed , who leads Gallup 's education work : `` If you can go to Podunk U debt free vs. Harvard for $ 100,000 , go to Podunk . And concentrate on what you do when you get there . ''",
            "House Speaker Paul Ryan , at a private dinner earlier this year , said he thought only \u201c one member \u201d wanted to build a wall across the entire U.S.-Mexico border , \u2588\u2588\u2588 has learned from multiple sources with direct knowledge of the comments , including former Rep. Tom Tancredo ( R-CO ) .\nThe dinner , sources said , took place on the eve of the House \u2019 s passage of two relatively minor immigration bills at the end of June : Kate \u2019 s Law and sanctuary city reforms . The far wider reaching Davis-Oliver Act was tabled at the same time .\n\u201c Ryan told a group of Republicans he met with \u2026 that only one person wants a wall , \u201d Tancredo told \u2588\u2588\u2588 shortly after the dinner .\nTancredo took issue with the Speaker \u2019 s characterization of support for the wall within the House GOP . \u201c Of course he means only one person in his entourage and of the leadership , \u201d he told \u2588\u2588\u2588 . \u201c I know several people in Congress who want a wall and I know that there are millions of Americans who want a wall . \u201d\n\u201c You have to understand the level of fear that exists in the Republican establishment about this issue , \u201d Tancredo told \u2588\u2588\u2588 , seeking to explain the pressures that Republican members of Congress face when addressing immigration .\n\u201c The Chamber of Commerce doesn \u2019 t want a wall \u2026 the pressure is greater from the Chamber of Commerce than it is from the members , \u201d Tancredo , who for years in the House fought a mostly fruitless battle to get Congress to combat the flood of illegal immigration , added . \u201c That \u2019 s the basic problem . It was then . It is now . \u201d\nA current House GOP member confirmed that Ryan made a remark similar to the one Tancredo referenced , but stressed that the Speaker was attempting to summarize the disparate voices in the House GOP caucus , telling \u2588\u2588\u2588 :\nAll this narrative serves to inform is that Ryan \u2019 s is making a point of listening to Members and that Members mostly are trying to listen to each other . I believe it is true that support for the wall is not as strong as it needs to be among House Republicans .\nThat member added an assessment of the difficulties facing the effort to fund the wall . According to this member who supports a border wall , one of the biggest problems is Republicans \u2019 lack of knowledge of the history of the immigration issue and the failures to secure the border in the past . The House member told \u2588\u2588\u2588 :\nAnother thing I have noticed is that Members \u2019 knowledge and opinions on immigration seem to only be traceable back to their arrival in Congress . Not many brought much experience or knowledge on the topic with them . 64 % swore in January 2011 or later . They only know that which was debated in the Obama era . Some are Never Trumpers . We have work to do .\nThe office of Speaker Ryan and another House GOP member who \u2588\u2588\u2588 was told attended the dinner neither confirmed nor denied that Ryan made the comment about support for the wall .\nThe southern border wall is President Donald Trump \u2019 s signature campaign promise and the ability of the Republican-controlled Congress to deliver the authorization and funding will likely define the success or failure of the administration \u2019 s immigration agenda . As Tancredo put it to \u2588\u2588\u2588 :\nEvery rally [ the president ] would whip up the crowd saying we \u2019 re going to build a wall . And so you had hopes that in putting so much rhetoric into it during the campaign that it would be hard to avoid it \u2026 but so far they have found a way to do so .\nSo far , no funding has been forthcoming , with any mention of the wall dropped from the Spring \u2019 s GOP budget proposals . The White House itself was unclear as to when funding might be expected .\nRyan , interestingly , has been claiming that the House has funded the border wall this year . But , the claims from his office that the House-passed funding measure \u201c fully funds the Trump administration \u2019 s request for a wall along the southern border \u201d are misleading at best . What Ryan \u2019 s office is referring to in that release , sent out on Tuesday , are the 12 appropriations bills . Those will not become law , because Ryan and Senate Majority Leader Mitch McConnell failed to get them passed out of both chambers of Congress and onto the president \u2019 s desk . As such , President Trump cut a temporary deal with the Democrats to avert a government shutdown and raise the debt ceiling in a joint package .\nTancredo was pessimistic the congressional Republican leadership can be easily brought on board with the immigration agenda of the president and the party \u2019 s conservative wing . According to him , Ryan , who was caught on tape after the emergence of the now-infamous Access Hollywood recording of the President saying he was , \u201c not going to defend Donald Trump\u2014not now , not in the future , \u201d would rather lose elections to Democrats than seriously address the issue of illegal aliens .\n\u201c Ryan and the Senate Majority Leader [ Mitch McConnell ] would rather have had Hillary than Donald Trump for that very reason , \u201d Tancredo told \u2588\u2588\u2588 . \u201c They failed at stopping him and now they \u2019 re going to have to stop him legislatively . \u201d",
            "( CNN ) President Donald Trump has reason to hope his luck is changing after a long legal losing streak .\nTrump got to celebrate a big win Wednesday in an emoluments clause case relating to his Washington hotel . And there are signs that a case in Louisiana could cause yet another near death experience for Obamacare , his predecessor 's top domestic achievement .\nThe courtroom action this week represents a potential reversal of fortune for Trump following a long list of defeats the President has tasted on cases from immigration to the 2020 census to his efforts to thwart Democratic oversight to his central campaign promise to build a border wall . For a man who bills himself as one of life 's ultimate winners , Trump 's legal losing record is a branding nightmare .\nYet the intimate relationship between this President and the courts actually goes beyond the win-loss calculation that normally powers Trump 's life . The judicial system serves multi-dimensional roles for Trump in his personal , business and Washington life .\nWhile the law has often frustrated Trump 's political goals , he has still used it as a weapon to combat Democrats , as the glue in his conservative coalition and to postpone threatening political crises .\nOften -- as in the case of Trump 's national emergency declaration designed to fund his border wall or the census -- it seems as if the long odds in court do not deter the President . The law gives Trump another venue for the endless fights that sustain his politics and his personality . Even if he loses he is showing his supporters he 's never giving up the battle .\nTrump 's judicial appointments are likely to shape the character of American life for years after he 's left the White House . And it 's still possible court rulings could pose an existential threat to his personal and business legacy given the flurry of cases currently open in New York .\nAs is often the case , Trump 's wins in the courts have been outnumbered by his losses this week .\nThe administration has just tumbled to defeat before different judges -- including in the Supreme Court -- on its attempts to place a citizenship question on the 2020 census .\nTwo significant court rulings in May upheld Congress in its battle to subvert Trump 's war on oversight over Democratic lawmakers ' efforts subpoena his financial records .\nTrump has also tasted defeat in huge cases on immigration -- slowing or thwarting his efforts to build his border wall , and right at the start of his term on his original travel ban . The Supreme Court has since allowed parts of a rewritten plan to stand .\nResearch by the Center for Policy Integrity at the University of New York School of Law showed that the administration had won only three of 42 deregulatory cases , a paltry success rate of only 7 % .\nYet Trump 's relationship with the courts is actually far more complicated than the win-loss ratio with which he judges his own success and that of everyone around him .\nIn decades as a businessman Trump was the initiator and the target of thousands of lawsuits . He used the courts to try to extricate himself from dicey situations , as a weapon in negotiations and to test the legal limits of business practice .\nHe used lawsuits to save face , to offer a new venue to prolong a fight , to put off a reckoning or agreed out-of-court settlements to limit the costs of personal and business liabilities .\nAs President , Trump has also used courts to fulfill wider goals than simply winning and losing cases , especially since he 's struggled to get many major bills through Congress -- apart from a big tax reform program .\nWith bold assertions of executive power , Trump has made the courts a constant presence in his presidency .\nWhen he 's won , he 's trumpeted it . When -- more often -- he loses , the judgments become exhibits in his foundational political case that an elite establishment is out to get him and that he 's being treated unfairly .\n`` So now the Obama appointed judge on the Census case ( Are you a Citizen of the United States ? ) wo n't let the Justice Department use the lawyers that it wants to use . Could this be a first ? '' Trump tweeted after a reverse in the census case on Tuesday .\nHis frequent complaints about `` Obama judges '' reveal his view that the courts are simply an extension of the political game and earned him a rebuke from Chief Justice John Roberts .\nAdministrations often try to achieve through the courts what they can not legislatively -- and the Trump team along with allied GOP states has been especially enthusiastic in this regard .\nJust this week , in a hearing in New Orleans , two Republican-appointed appellate judges appeared to suggest in oral arguments that a fresh challenge to Obamacare could succeed .\nThe case also reflects the manner in which , in an era of congressional stasis and polarization , courts are being called upon to do the job lawmakers might once have done .\nJudge Kurt Engelhardt questioned why , after a US district judge declared the whole ACA unconstitutional , Congress did not pass a law clarifying what provisions should stay on the books .\n`` Why does Congress want the ... judiciary to become the taxidermist for every legislative big-game accomplishment that Congress achieves ? '' Engelhardt asked .\nThe administration 's legal gambits have often reflected the chaos and politicized arguments that rock the administration every day and have sometimes hampered its own chances of success .\nLast week , for instance , a Justice Department lawyer admitted he had no idea what was in Trump 's mind when he suddenly reversed course on the census case on Twitter .\nJUST WATCHED Justice Department changes step following Trump 's tweet Replay More Videos ... MUST WATCH Justice Department changes step following Trump 's tweet 01:51\nSometimes , Trump has turned to personal litigation to try to frustrate his political enemies .\nIn March , Trump personally sued his own accounting firm and the chairman of the House Oversight Committee to try to stop the handover of his financial records .\nThe President has sometimes been the target of litigation as well : Democrats are increasingly turning to the courts to enforce subpoenas .\nA huge test of presidential authority is looming over Trump 's sweeping claims of executive privilege that may eventually work their way up to the highest courts .\nThe cases could eventually lead to profound rulings about the scope of presidential power that could resonate for decades to come . And if Trump were to refuse to hand over documents or tax returns ordered by the courts , he could turn overused predictions of a looming constitutional crisis into reality .\nTreasury Secretary Steven Mnuchin 's refusal to hand over Trump 's tax returns to a House committee under a provision of the tax code is likely to spark a long and costly court fight .\nThat 's an example of where legal action suits Trump just fine .\nIn such cases there 's a good chance he will fail on the merits -- but the law 's slow march means that he 's at least putting off a threatening political situation for another day -- possibly even beyond the 2020 election .\nEach new challenge becomes a new example of the `` presidential harassment '' -- the term Trump and his allies use to stoke a sense of victimhood around his administration and to solidify his support with his all-important political base .\nWhile the President may feel that he has a good chance of evading the worst possible outcome of Robert Mueller 's special counsel probe -- he may not be out of the legal mire yet .\nTrump is facing multiple civil and criminal investigations of his business , financial affairs , personal conduct , his foundation and inaugural committee .\nJUST WATCHED Supreme Court to decide future of DACA Replay More Videos ... MUST WATCH Supreme Court to decide future of DACA 01:29\nThe political synergy between Trump and the courts has an even deeper connection to his presidency than cases in which he is embroiled .\nThe President 's decision to publicize a list of potential Supreme Court justices vetted by the Federalist Society was in retrospect one of the smartest moves of his 2016 campaign , embedding evangelical and judicial conservatives into his support base despite doubts about his character and ideology .\nTrump has delivered on his vows to build a conservative majority on the Supreme Court with the seating of Justices Neil Gorsuch and Brett Kavanaugh . The court 's new ideological balance means that rulings favorable to Trump 's leanings on everything from deregulation to abortion could be handed down for years to come .\nAnd the President 's alliance with Senate Republican Majority leader Mitch McConnell has been confirming conservative judges to lower courts at an impressive clip .\nAccording to the Heritage Foundation 's Judicial Appointments Tracker , Trump has installed 127 federal judges -- more than President Barack Obama 's figure of 89 at the equivalent point in his presidency .\nThere is no guarantee that such judges will necessarily share Trump 's challenging and unique interpretations on the limits of presidential power .\nBut some of them could provide a more ideologically friendly judiciary for Trump 's policy efforts if he wins a second term and could help break his losing streak .\nAnd the Trump class of judges at all levels of the federal bench is likely to frustrate a future Democratic president .",
            "The controversial immigration-reform bill that passed the Senate Judiciary Committee this week is expected to be considered by the Senate in June . Many see measures contained in this bill , such as a strong E-Verify and a \u201c photo tool , \u201d as a means to control unlawful immigrants \u2019 access to unlawful employment . I worry that they go too far .\nI think there are better ideas that err on the side of individual privacy while still strengthening our borders . We should scrap a national identification database and pass immigration reform that secures the border , expands existing work-visa programs and prevents noncitizens from access to welfare . These simple ideas will eliminate the perceived need for an invasive worker-verification system and a government citizenship database .\nI am against the idea that American citizens should be forced to carry around a National Identification Card as a condition of citizenship . I worry that the Senate is working to consider a series of little-noticed provisions in comprehensive immigration reform that may provide a pathway to a national ID card for all individuals present in the United States \u2014 citizens and noncitizens . These draconian ideas would simply give government too much power .\nForcing Americans to carry around an identification card to affirmatively prove citizenship offends our basic concept of freedom . Wanting to avoid a \u201c papers please \u201d culture in our country is also why conservatives oppose federal universal gun background checks . We oppose such measures not because we don \u2019 t believe in common-sense rules or regulation \u2014 but because we are wary of giving the federal government this kind of centralized power over our daily lives .\nI am against government lists of those who own or have transferred a firearm for the same reason I oppose any pathway to a national ID . I don \u2019 t think that government should have the awesome power of monitoring the legal activities of American citizens . That is not a proper role of the federal government \u2014 or any level of government , for that matter .\nI am opposed to immigration reform that contains the photo tool that is contained in the Interior Enforcement and Employment Verification System title of the bill . In the name of preventing the \u201c unlawful employment of aliens , \u201d the Senate legislation has a provision that \u201c enables employers to match the photo on a covered identify document provided to the employer to a photo maintained by the U.S . Citizenship and Immigration Services database. \u201d This , too , is troubling .\nThis sounds like a national picture database of all citizens , where the states house the picture and the Department of Homeland Security is the clearinghouse for worker verification . A national database of citizens raises the question : What activities will require someone to present their papers ? A national ID allows more power to gravitate to Washington and a greater likelihood that power will be abused .\nI will fight to remove the photo tool from this legislation because I think it will become a national ID . We already know the federal government is rife with false positives on the no-fly list and the National Instant Check system for gun buyers . Why would we be foolish enough to think that a massive database of all citizens would not have the same problems on a grander scale ?\nWe have a Second Amendment that must be protected . We also have a Fourth Amendment that must be protected . Citizenship means that the government is supposed to protect our rights , not take them away . We must have stronger borders , but there \u2019 s no reason we can \u2019 t have better security while respecting constitutional limits and liberties .\nIn the past week , we have witnessed examples of the Obama administration spying on the media and Internal Revenue Service discrimination against Tea Party free speech . People around the world always have dreamed of emigrating to America , the Land of the Free . It is our job to make sure our country stays that way .\nSen. Rand Paul , Kentucky Republican , is a member of the Senate Foreign Relations and Homeland Security committees .",
            ]

batch = tokenizer(raw_input, padding='max_length', truncation=True, max_length=512,return_tensors="pt")
outputs = model(**batch)
logits = outputs.logits
prediction_score = nn.functional.softmax(logits, dim=-1)
prediction_label = torch.argmax(logits, dim = -1)
print(prediction_score)