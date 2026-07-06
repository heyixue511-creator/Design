# The Ethnographic Interview in User-Centered Work/Task Analysis

Larry E. Wood

Brigham Young University

![](images/5343e98493c1146b16c9fd30872796746c1a67cd7c90039f02de56b311cf4472.jpg)

## EXECUTIVE SUMMARY

An interviewing strategy for work/task analysis of potential clients of software support applications is described herein. It draws on methods from the disciplines of Ethnography and Cognitive Science. The ultimate goal is to produce a descriptive model of current work practice that can be used in user-centered design of a software application. The interviewing strategy is characterized as a top-down approach where semistructured interviews are used to develop a framework for guiding direct observations of real work. Various types of questions are introduced that are designed to be used by analysts in an opportunistic fashion to suit the particular analysis goals. It is recommended that the interviews focus initially on the identification of work objects, their relationships, their categories, and their discriminating features. That information can then be used to develop task representations in which the relevant objects are used by clients to accomplish their work. Suggestions are provided for describing and documenting a work model.

## BACKGROUND

In a recent article Hughs, King, Rodden, and Anderson (Hughes et al.   
1995) discussed the role of Ethnography in interactive systems design.

One of the points made by those authors was that "Ethnography has a role to play in various phases of system design and makes different contributions to them." Whereas the issues addressed by the authors are of a general nature, the work reported here focuses specifically on the ethnographic interview and its potential role in the design process. The techniques described are adaptations of those developed by myself and my colleagues previously for use in knowledge elicitation for knowledgebased (expert) systems (Wood and Ford 1993; Ford and Wood 1992).

The interviewing techniques are described in the context of a software development project in which I have been involved. The purpose of the application is to expedite the ordering of telecommunication services (telephone and electronic network services) for all departments on the campus of Brigham Young University. Each academic or support unit has a designated representative to coordinate ordering of Telecommunication services (Telecom Services) for their unit. Currently, orders were processed via memoranda, following telephone and face-to-face negotiation between the unit representative and a representative from Telecom Services.

A design team for the project was organized, consisting of the manager of the Telecom Services department, the department's chief analyst/programmer, myself (acting as a usability analyst/interaction designer), and five potential clients of the order application. The clients varied widely in their experience and scope of responsibility. Experience varied from less than a year to more than ten years, and scope of responsibility varied from a small academic department (15 faculty and staff) to the entire Law School (approximately 700 faculty and staff).

## GUIDING PRINCIPLES AND WORKING ASSUMPTIONS

Although the focus of this article is on interviewing techniques, I do not mean to imply that interviews are adequate and sufficient for meeting all the needs of work/task analysis. As I will discuss, it is also vitally important to observe clients doing work in their natural settings and to gather and document examples of real work. It is my goal to place ethnographic interviewing in the broader context of interaction design and to provide guidelines for making client interviews as productive as possible while also providing some concrete examples of the application of those guidelines.

The general framework presented here, in which ethnographic interviewing is embedded, I characterize generally as a top-down approach. This is in contrast to a bottom-up approach, which would be more characteristic of various versions of Contextual Inquiry (Wixon and Holtzblatt 1990; Holtzblatt and Beyer 1993). I refer to my approach as top-down because I use semistructured interviewing with clients prior to doing systematic observations of work. Doing so provides a general framework in which to interpret and document specific observations and samples of real work. On the other hand, I refer to Contextual Inquiry as a bottom-up approach because of its usual emphasis on first observing and gathering large samples of real work (i.e., collecting data), and then inductively abstracting work flows and other more general descriptions of the work/tasks being analyzed (i.e., analyzing the data).

In performing work/task analysis, I find it particularly important to consider what is generally understood about the nature of expertise, because potential clients of an application are experts in the work which the software application is intended to support, whether or not they are considered experts in the use of computer software. Therefore, it is important to recognize and respect their point of view throughout the development cycle. As suggested by LaFrance (1989), one reason that work/task analysis can be such a difficult problem for analysts is because they continue to underestimate the complexity of expertise in a given domain of knowledge. There is also a body of literature in cognitive psychology (Reimann and Chi 1989) on the nature of expertise that has implications for how one should work with experts to gain an understanding of how they accomplish their work in a specialized domain.

Important aspects of expertise that I find particularly relevant to work/task analysis are the organization of expert knowledge, the tacit nature of expert knowledge, the problem of simplification bias on the part of interviewers, and the exercise of translation competence on the part of experts. Each of these aspects will be described, and then they will be specifically addressed relative to particular interviewing techniques discussed later.

## Organization of Expert Knowledge

Because concepts in human memory are obviously associated with one another, the experience of remembering or being cued with one concept results in the recall of additional relevant concepts. It is helpful to keep in mind that studies (Mitchell and Chi 1984) have shown that expert knowledge is generally organized hierarchically, at a macro level (i.e., using various taxonomic organizations such as categories and subcategories) although many other types of relationships are also present, depending on the particular domain of expertise. At the micro level, expert knowledge is stored as organized "chunks" of frequently occurring patterns or schemas (Chi et al. 1981), with attached procedures for appropriate responses when those patterns are recognized in problem-solving situations.

In relation to the nature of the organization of expert knowledge, I have found it useful to distinguish between object knowledge and process knowledge. Object knowledge includes the conceptual entities and objects (both concrete and abstract) in a particular domain and their various relationships and categories. Taxonomic relationships (such as types and subtypes, parts, and distinguishing features or characteristics) are particularly important. Process knowledge, on the other hand, is comprised of the knowledge required for solving domain problems using relevant domain concepts and objects. Another way to characterize this distinction is a knowledge of"what" versus a knowledge of "how." As described later, I structure interviews for work/task analysis around this distinction.

## Tacit Knowledge

It is a common observation that much of an expert's problem-solving knowledge has become automatic or tacit through extensive use, and there has been considerable debate about its accessibility, even to the expert (Ericsson and Simon 1993). In early stages of skill learning, an individual consciously considers various items of knowledge during problem solving. In well-learned tasks, much of the relevant knowledge is no longer consciously available during problem solving, although this does not mean that it has been "forgotten." It does mean that it may be difficult for an expert to articulate it, especially when asked to do so directly, independently of, or even during task performance.

While direct access to tacit knowledge may not be feasible, it is often possible for an analyst to use information about an expert's view of the domain to constrain inferences about tacit knowledge. As discussed later, tacit problem-solving knowledge often manifests during observation of actual problem-solving episodes.

## Simplification Bias and Translation Competence

Because an analyst is often a relative novice in the problem domain being analyzed, there exists a potential for errors because of a tendency for the analyst to conceptually simplify the descriptions of problem solving provided by the expert. In an attempt to minimize the potential effects of this “simplification bias," the interviewing techniques described here have been adapted from the disciplines of Ethnography (Spradley 1979; Werner and Schoepfle 1987) and Cognitive Anthropology (Anderson and Alty 1995) because researchers in those disciplines face a similar problem when they are attempting to elicit cultural information from informants (or cultural "experts") in unfamiliar societies. Spradley (1979) makes a convincing case for the importance of domain-specific language in this effort. He notes that potential bias can be particularly critical when the members of a culture under investigation use terms familiar to the researcher, because important differences in the meanings of the terms are not readily apparent to the researcher.

Spradley (1979) describes another potential source of bias, which he terms the exercise of translation competence . In contrast to simplification bias, which occurs on the part of an interviewer, translation competence is a characteristic of the cultural informant. It is expressed when informants translate the reality of their culture in order to explain it to an outsider. The problem is that the more an informant translates for the convenience of an investigator, the more the cultural reality becomes oversimplified and distorted.

In an effort to avoid translation bias, Spradley (1979) advocates an approach to questioning which makes minimal assumptions (on behalf of the researcher) about informants'knowledge and uses information the informants provide as the basis for further questioning. The researcher first uses very general probing techniques to persuade informants to talk freely about their domains in a global sense. An informant's language is recorded and then examined for category labels and other linguistic cues that are domain-specific. This information is then used to probe informants for additional information. Throughout the process it is necessary to verify that the researcher's emerging understanding of the domain accurately reflects the informant's expertise. For this reason, the interviewing strategies described here are considered semistructured rather than structured. Rather than designing a priori a specific set of questions to be to be asked in a specific order, analysts have various types of questions at their disposal to be used in opportunistic ways, depending on the demands of the situation.

## INTERVIEWING STRATEGIES

As indicated earlier, this approach draws heavily upon ethnographic methods, but also makes use of techniques from cognitive psychology (Anderson 1994). Furthermore, it is centered around the distinction between object and process knowledge (described earlier). The goals of work/task analysis to be supported by the interviewing techniques described here are similar to those of Contextual Inquiry: to develop a work model describing clients'current work practices, and then to develop an enhanced work model (proposing ways in which the clients' work can be re-designed and enhanced by introducing a software support application). The latter model then is intended to provide a basis for the design of the application (both the underlying functionality and the user interaction/interface) to provide access to that functionality.

## Object Identification

Because much of the information about relevant objects and their related categories and concepts is reflected in a client's use of domainspecific terminology, a significant amount of the analyst's early efforts should be spent documenting the client's use of work-related language. It is important to remember that a word or phrase need not be obviously unfamiliar to the analyst in order to be important. For example, in the domain of Telecom Services, the term ethernet port might have little meaning to an analyst unfamiliar with a networking domain, and would be an obvious point of focus in an interview. What might not be obvious, however, is that the term data connection has special significance in this domain (i.e., a connection from a computer workstation to the campus network through a Rolm telephone set), because most analysts would be familiar with the term data and might mistakenly assume their understanding of the term applies in this context. Thus the analyst should attend particularly to all terms and phrases that are used frequently by the client to make certain that such assumptions are tested.

The goal in the early stages of interviewing is to direct the client's attention toward the task of describing the structure of the work domain (e.g., objects and their relationships). It is important for the analyst to arrange for the client to describe the work practice in a natural way, using domain-specific terms for important objects. However, the analyst must also be concerned about keeping the client focused on that portion of the work that has been targeted for analysis. Otherwise, the interview can meander and become inefficient. It is, therefore, important for the analyst to be guiding the general direction and flow of the interview, while letting the client freely and naturally express her/his conceptualization of it. Specific types of questions are designed to assist the analyst in meeting these goals.

One way to elicit a large sample of work-related terminology is to ask Grand Tour questions, which encourage the client to verbally "show the analyst around" the physical, temporal, and abstract space of the work domain. Table 3.1 shows specific examples of such questions.

Grand Tour questioning is of particular utility early in analysis, but can be used whenever the client identifies a new subproblem. I have found the most useful types of Grand Tour questions to be Task-Related and Guided questions (see Table 3.1). Because the analyst's ultimate goal is to understand the tasks (and task interrelationships) required to perform some set of a client's work, these types of questions help keep the client focused on relevant aspects of the work domain, without causing too narrow a focus too early. Asking about typical problem-solving episodes (using Typical questions—see Table 3.1) often elicits general categories used in frequently occurring situations.

Case-Focused questions (see Table 3.1) are also useful in eliciting domain terminology. Cases are indexed in memory by the categories of which they are members. These types of questions elicit further terminology used to characterize work-related objects by evoking the client's description of the characteristics and details of particular problemsolving episodes. They also provide a basis for keeping an interview focused on relevant topics, especially if a client tends to get sidetracked. Obviously, Case-Focused questions require reference to specific examples of work and provide the basis for further questioning about process knowledge, as will be discussed later. Their main function in early stages of analysis is to provide cues for retrieval of information about work-related objects, abstract as well as concrete.

TABLE 3.1 Object Identification Questions.
<table><tr><td>Question Type</td><td>Example</td></tr><tr><td>Grand Tour:</td><td></td></tr><tr><td>Task-Related</td><td>&quot;Could you discuss the major steps you go through in filling a request for services from a member of your unit?&quot;</td></tr><tr><td>Guided</td><td>&quot;Could you show me one of the previous orders you have placed, and point out the different parts?&quot;</td></tr><tr><td>Typical</td><td>&quot;Could you tell me about a typical request from one of the members of your unit?&quot;</td></tr><tr><td>Case-Focused:</td><td></td></tr><tr><td>Example</td><td>“Can you show me an example of a face plate template?&quot;</td></tr><tr><td>Personal Experience</td><td>&quot;You&#x27;ve probably had some interesting experiences dealing with requests for face plate configurations. Tell me about some of them.&quot;</td></tr><tr><td>Native-Language:</td><td></td></tr><tr><td>Direct Language</td><td>&quot;What do you call the buttons that allow one to select a particular line on a set?&quot;</td></tr><tr><td>Hypothetical-Interaction</td><td>&quot;How would you describe the various types of jacks to another Telecom services liaison?&quot;</td></tr><tr><td>Use</td><td>&quot;What purpose does the auto-intercom feature serve?&quot;</td></tr></table>

Example questions (see Table 3.1) help the analyst to obtain more detail about terms that are already identified. Personal Experience questions (see Table 3.1) are also useful for this purpose, but can be a source of distraction if used too early in analysis. The most useful domain abstractions for early analysis are those that are relevant to many potential situations in a domain. Hypothetical-Interaction questions provide the analyst with indirect access to a larger "community" of domain experts. Communication about domain problems and knowledge between experts within this community is one of the processes that fosters the development and use of specialized domain terminology, or jargon (Spradley 1979).

Although most of the Object Identification questions are designed to elicit natural domain descriptions in a rather indirect way, there will undoubtedly be times when this strategy will fail. As discussed earlier, Spradley (1979) warns that cultural experts tend to translate their knowledge into terms they believe the interviewer will find easier to understand. Direct Language questions (see Table 3.1) can be used when this is suspected.

One technique often used by ethnographers to elicit informants' natural descriptions of terms and concepts is to ask how terms, tools, and concepts are used rather than what they are or mean. Direct questions about meaning tend to encourage the expert to translate. Queries about Use (see Table 3.1) prompt the informant to describe the context in which a particular term or object plays a role. This description provides information which can be used to structure even more in-depth questioning.

Perhaps the most important technique, given our focus on language, is to phrase questions to a client in domain-specific terminology. An analyst's consistent use of terminology different from that of the client will encourage the client to translate. Using the domain-specific language, however, provides a context of familiarity and encourages a client to focus on the work domain itself rather than the analyst's methods and unfamiliarity with the domain.

Whenever possible, it is preferable to interview clients in their natural work setting, i.e., the setting in which the expert usually solves problems (Bell and Hardiman 1989; Holtzblatt and Beyer 1993). The familiar surroundings serve as further cues to the knowledge clients use in performing their work. There is evidence (Mitchell and Chi 1984; Werner and Schoepfle 1987) indicating that individuals select a limited number of all possible associations for report in any given interviewing context. It would be premature to conclude that knowledge about a given term or topic is tacit and completely unavailable to clients simply because they fail to respond in a particular questioning context. Rather, it is advisable to extend questioning about each term over a number of interviewing contexts in order to maximize the total amount of information retrieved.

## Object Relationships

In order to identify the relationships among domain categories and objects, an analyst can use questioning techniques that explore the rich, integrated organizational structure of a client's knowledge. These techniques are based on the general principle that concepts in memory are associated with one another, and that remembering or being cued with one or more domain concepts will result in the recall of additional, related concepts.

As discussed earlier, an important strategy, given the focus on language, is to phrase questions to the client using domain-specific terminology that has already been obtained in responses to previous questions. For object relationships, an analyst needs to look for category labels. A particular category term may be associated with a number of subcategories, each of which are related to the category label by a particular functional relationship. Examples of Object Relationship questions are presented in Table 3.2.

Suppose, for example, in answer to the task-related Grand Tour question listed in Table 3.1 above, a Telecom Services coordinator replied "I ask department members if they will need any network applications, in addition to their normal types of telephone use." This statement indicates that there are at least two subcategory terms in the domain defined by the category term use and the semantic relationship types. These two entities are alike in that both are types of telecommunications use, and it is likely that the client can provide further information about other types and make meaningful distinctions among them.

The most fruitful way of eliciting such domain structure is to first identify the category label and functional relationship from a sample of a client's language elicited through Object Identification questions (see Table 3.1). Then the analyst should elicit a list of category members by asking Category Member questions (see Table 3.2). Any objects for which the analyst is uncertain regarding category membership can be clarified by asking additional Category Membership questions. Once the client indicates that there are no more members in a particular category, the analyst should elicit the relevant features and dimensions of contrast that discriminate the members of a category from one another in meaningful ways for work. This is accomplished by asking a number of Contrast questions (see Table 3.2). As before, it is important to attend to the client's terminology for these dimensions and features.

The best place to begin building domain hierarchies may be with basic-level domain terms (Lakoff 1987; Rosch 1973), which can be tentatively identified from their frequency of use by the client, their lexical brevity (note the prevalence of acronyms and other abbreviated forms in the jargon of many domains), and, to a lesser extent, by their unfamiliarity to the analyst. The use of Contrast questions (see Table 3.2) for more information at this level exploits the larger number of distinctions and associations to these key concepts in an expert's memory.

Limiting requests for distinctions to contrast sets of category members helps an analyst avoid the problem of eliciting artificial distinctions. Ethnographers have found that informants will give test question responses in an attempt to provide the right answer, and will sometimes identify distinctions that are real, but not actually relevant to the use of the objects. A constant focus on the structure of a client's work-related knowledge is an attempt to avoid this difficulty. At this point, it should be noted here that although I have emphasized categorical relationships in this discussion, there will obviously be other important relationships that must be understood (e.g., part-whole, attributes, and cause-effect), depending on the domain under study (Reigeluth et al. 1994) .

TABLE 3.2 Object Relationship Questions.
<table><tr><td>Question Type</td><td>Example</td></tr><tr><td>Relationship:</td><td></td></tr><tr><td>Category Label</td><td>&quot;What are the different types of telecommunication uses?&quot;</td></tr><tr><td>Category Member</td><td>&quot;Are network apps and FAX/Card Readers both types of telecommunications use?&quot;</td></tr><tr><td>Contrast:</td><td></td></tr><tr><td>Directed Contrast</td><td>&quot;Could you look through this order memo and show me what other items are considered network apps?&quot;</td></tr><tr><td>Dyadic Contrast</td><td>&quot;What differences are there between intercom groups and pick groups?&quot;</td></tr></table>

I would like to note that although Object Identification questions and Object Relationship questions have been discussed in different sections, I do no mean to imply that the information should be sought from clients in any rigid order. As suggested earlier, the advantage of semistructured interviewing is that various types of questions can be used opportunistically. I usually find it convenient to mix the two types of questions to suit a particular situation and set of goals.

## Work Model Development and Documentation

I prefer to limit my interviews to approximately an hour, and I tape record each one for later analysis and interpretation. I prefer not to interrupt clients, and I find that I simply can't capture all that they are telling me without doing so. Therefore, during the interview, I take only enough notes to keep it flowing. Following each interview, I review the tapes and my notes, and analyze and document the results. I then ask the client to review the description prior to the subsequent interview. At the beginning of each subsequent interview, I invite the client to make note of my errors in interpretation, and then we continue to extend and expand the model appropriately. See the Appendix for a detailed account of the methods used in interview analysis, a description of work model development, and a description of the work model.

## Process Knowledge

Once a large portion of the Object knowledge has been modeled, the analyst can proceed to an examination of how clients use the objects and their categories, distinctions, and attributes to accomplish their work. It is useful at this stage to bear in mind two of the characteristics of expertise. First, it has been shown (Chi et al. 1981) that experts represent problems at a level of underlying principles and abstractions. Second, the strategies that experts use in solving problems are sometimes common across domains, and are sometimes domain-specific (Reimann and Chi 1989). The particular representations and strategies are often elusive and must be explicitly sought by a variety of methods.

Perhaps the most widely used technique developed in cognitive science to investigate problem solving strategies is think-aloud protocol generation and analysis. The term "protocol analysis" represents a family of techniques used to examine subjects'verbalizations about their problem-solving processes. Ericsson and Simon (1993) have observed that the analysis of a verbal protocol must be preceded by a domain definition phase, during which the researchers must exhaustively catalogue the labels for objects, concepts, etc. referred to in the protocol. This is consistent with my concern regarding object knowledge.

While one obviously could begin a work/task analysis with thinkaloud protocols generated in the context of work-related tasks I have found it most useful to first obtain a preliminary understanding of the relevant work objects, as described earlier. Following this, it has proven considerably easier to understand how the objects are used in workrelated tasks and procedures, rather than attempting to understand the objects as well as the procedures used on/with them concurrently. As I use them, methods for protocol generation simply become additional interviewing techniques. Reasoning and problem-solving strategies emerge from a variety of think-aloud protocols generated by asking clients to describe their thought processes as they solve specific work problems or cases.

There are at least three types of protocol-generating procedures that have been used in studying problem solving. As shown in Table 3.3, Concurrent Think Aloud questions simply request an expert to report the contents of conscious awareness during the solution of a domain problem. Ericsson and Simon (1993) caution that this procedure can only yield meaningful results when the task being performed concurrently with the protocol does not require the use of verbalization or other processes that tax the resources of working memory. Even when this condition holds, a problem solver is likely to provide an incomplete account of the moment-to-moment contents of consciousness. Information that is processed automatically will often not be reported at all. However, these results will still be valuable, because they provide information about the sequence in which the expert attends to various problem features and the various subgoals for which these features are relevant.

Aided Recall questions (see Table 3.3), which are a type of retrospective (rather than concurrent) protocol generation, can be used to followup results obtained in concurrent think-aloud protocols. This technique, which has been used successfully in eliciting descriptions of expertise (Kuipers and Kassirer 1983), involves video- or audio-taping the performance of an expert engaged in problem-solving and then reviewing this record with the expert at a later time, with emphasis on her/his thoughts at a particular stage of problem solving. This procedure creates a situation in which recall of processing is cued by an unbiased record of the expert's own performance. A variation on aided-recall, called cross-examination (see Table 3.3), has been used successfully by Kuipers, Moskowitz, and Kassirer (1988) to probe the limits of knowledge directly. After completing a concurrent thinkaloud protocol on a particular problem, the expert is asked specific questions about it, particularly aspects that seem vague or uncertain to an analyst.

In developing work/task models of clients'work, the problems clients attempt to solve are obviously those that define the designated work. Therefore, any use of protocol generation should be done in the context of that work. It should be obvious in the context of any clientcentered design approach that observations would be of real work episodes (specific examples of work tasks) from which more general descriptions can be derived.

Process knowledge, like object knowledge, must be represented in some manner in a work model description for future reference by the analyst and other members of the development team, especially clients. Particularly for review purposes, I have found it helpful to represent work/task descriptions both at an abstract/summary level and at a more detailed level. For the abstract level, I currently use structured outlines, an example of which is found in Figure 3.4 of the Appendix (see the Appendix for additional information regarding the analysis and documentation of process knowledge). For more detailed descriptions, some form of scenario development is very important (Carroll 1995). I find it particularly important to have representations that are understandable to the clients whose work is being modeled. Otherwise, it is very difficult for them to verify that the task/work models are valid and complete, from their perspective.

TABLE 3.3 Think Aloud Protocol Generation Questions.
<table><tr><td>Question Type</td><td>Example</td></tr><tr><td>Concurrent Think Aloud</td><td>&quot;Think out loud while you generate an order for adding an ethernet connection to a faculty member&#x27;s office as described in this request. Do not worry about talking in complete sentences or</td></tr><tr><td>Aided Recall (retrospective protocol)</td><td>making sense.&quot; &quot;As we review this tape of the order you just generated, say whatever you remember about what you were thinking. Stop the tape or rewind</td></tr><tr><td>Cross-Examination</td><td>whenever you want.&quot; &quot;How did you decide which type of jack splitter to request for the installation of this new ethernet connection?&quot;</td></tr></table>

I document segments of task descriptions as they emerge during early phases of analysis (as might be the case when asking a taskrelated Grand Tour question originally intended to stimulate a client to talk about work-related objects), and then I fill out details through think-aloud protocols generated in the context of specific cases or examples. They are then validated against specific work examples, as discussed below.

## WORK MODEL VALIDATION

It should be obvious that a constant concern during work/task analysis is to develop a valid model of the work performed by clients, including the ways they think about itwhich a potential application will support. There are, of course, limitations to what can be obtained using the interviewing techniques discussed here and any resulting static description, with its combination of verbal and graphic representations. That is, of course, why is it important to conduct the interviews in the normal work context when possible, with a client being able to refer to work objects and artifacts during the interview. As discussed earlier, I prefer to conduct a series of interviews, approximately an hour in length, with time in between to analyze the results, update the work model description, and allow the client to review it prior to a subsequent interview.

It is imperative that the work model be based on real work episodes and products. Not only does this help ensure accuracy of the work model in early stages of development, but the examples and products (as long as they are reasonably representative) can be used to verify a final version of the work model and to develop more general scenarios. If the model can run with examples of real work, then the analyst can be reasonably confident about its validity at that stage of development (Johnson et al. 1995). Furthermore, those examples (and scenarios developed from them) can be used to verify decisions across further stages of development (e.g., interface prototyping and formal usability testing of a running application).

A strategic question that I have not yet addressed has to do with combining the results of interviews from various clients. In the case of the Telecom Services order application described here, I chose to work extensively with one client to develop a comprehensive model of the work involved in constructing orders. Copies of the description of that model were then circulated to the other members of the development team, and they were asked to review it. The client members of the team were asked to add their particular perspectives during individual interview sessions with each of them, in turn. Those different perspectives were then incorporated into a revised model and recirculated to all members for their further comment. A final interview was then conducted with each member of the team, and further revisions were made to the model until we collectively arrived at a composite work model with which everyone was satisfied. Appended to the final version of the model were scenarios and samples of representative orders previously requested by various clients. In addition, various suggestions from team members about how an application could enhance the ordering process were also appended.

Combining the interview results from multiple users the way I have described has, of course, both advantages and disadvantages. The biggest advantage is its efficiency, compared to the time required to develop complete work models independently with several clients and then to combine them into a representative composite model. A disadvantage is the risk of biasing the responses of all but the first interviewee, which goes against one of the basic tenets of the ethnographic approach. I have not collected formal data on this question, but I have found this to be another area in which samples of real work and their resulting products play an invaluable role. That is, an analyst must be attentive when a work sample from a client different from the one with whom the initial model was developed doesn't coincide with the initial description of the model. That is an indication of a potential bias. Further work with the new client can potentially correct the omission or error in the composite model. Most often, in my experience, the differences do not arise from bias or conflict among the various clients, but are a result of nonoverlapping areas of their work experience.

## SUMMARY

I have described a methodology for structuring interviews with clients for modeling their work in early phases of application development. I have developed my approach by importing and adapting methods from disciplines that have a history of related activities. In doing so, I have been influenced by several considerations. First, I have been guided by the nature of expertise, some important aspects of which are:

1. A high degree of tightly integrated domain-specific knowledge.

2. The fact that a substantial portion of the knowledge is tacit and difficult to articulate.

3. A potential for simplification bias on the part of an analyst.

4. The tendency for an expert to exercise translation competence.

The nature of expertise has led me to place a heavy emphasis on the use of work-related language in the interviewing methods to reveal the organization of expert knowledge and to avoid the potential sources of bias. The interviewing strategies are composed of various types of questions that can be used in an opportunistic manner in a series of semistructured interviews. Object Identification questions and Object Relationship questions are designed to explore the organization of domain concepts, objects, and their distinctive characteristics.

Another consideration guiding the development of my approach has been the early elicitation of object knowledge, which is then used to assist the understanding of process knowledge and the development of work scenarios. This is done primarily through the use of protocol-generation activities in the context of real work examples and products.

Finally, I have found it necessary to document and describe the work model iteratively, in a way than can be reviewed for verification by clients and other members of a development team. Adequate descriptions include both abstract summary forms of task representations (such as structured outlines and flow charts), and more detailed representations (such as work scenarios that can be used in validation of work models and in later stages of interaction design).

## ACKNOWLEDGMENTS

I wish to express my appreciation to other members of the development team for their cooperation in working with me in a research and development mode. Those individuals are: Ken Greer, Gary Buckway, Jennifer Chiara, Irene Fuja, Lynn Edwards, Carol Sant, and Alan Higley. The project was initiated by me as a research and development effort to allow me to apply some of my ideas on practice and process for usercentered design in the context of a serious development project, but one in which the final deadline was flexible.

I also wish to express my appreciation to Chris Pietras and Dennis Wixon for the valuable comments on earlier drafts of this chapter.

## REFERENCES

Anderson, B. and Alty, J.L. 1995. “Everyday Theories, Cognitive Anthropology and User Centered System Design." Proceedings of People and Computers X, HCI '95, August 29th-31st.

Anderson, J.R. 1994.Cognitive Psychology and Its Implications. San Francisco: Freeman.

Bell, J. and Hardiman, R.J. 1989. "The third role—the naturalistic knowledge engineer." Diaper D. (Ed.) Knowledge Elicitation: Principles, Techniques, and Applications. (pp. 49-85). New York: John Wiley & Sons, Inc.

Carroll, J.M. (Ed.). 1995. Scenario-based design: Envisioning Work and Technology in System Development. New York: John Wiley & Sons, Inc.

Chi, M.T.H., Feltovich, P.J., and Glaser, R. 1981. "Categorization and representation of physics problems by experts and novices." Cognitive Science, 5, 121–152.

Ericsson, K.A. and Simon, H.A. 1993. Protocol analysis: Verbal reports as Data (rev. ed.). Cambridge, MA.: MIT Press.

Ford J.M., and Wood, L.E. 1992. "Structuring & documenting interactions with subject-matter experts." Performance Improvement Quarterly 5, 2–24.

Gordon, S.E. and Gill, R.T. 1992. "Knowledge acquisition with question probes and conceptual graph structures." T.W. Lauer, E. Peacock, and A.C. Graesser (Eds.). Questions and Information Systems (pp. 29-46). Hillsdale, N.J.: Lawrence Erlbaum Associates.

Holtzblatt, K., and Beyer, H. 1993. "Making customer-centered design work for teams." Communications of the ACM 36(10), 93-103.

Hughes, J., King, V., Rodden, T., and Andersen, H. 1995. "The role of ethnography in interactive systems design." Interactions, II(2), 5–65.

Johnson, P., Johnson, H., and Wilson, S. 1995. "Rapid prototyping of user interfaces driven by task models." J.M. Carroll (Ed.), Scenariobased design: Envisioning Work and Technology in System Development (pp. 209–246). New York: John Wiley & Sons, Inc.

Kuipers, B.J. and Kassirer, J.P. 1983. "How to discover a knowledge representation for causal reasoning by studying an expert physician." Proceedings of the American Association of Artificial Intelligence. Los Altos, California: Morgan Kauffmann Publishers, Inc.

Kuipers, B., Moskowitz, A.J., and Kassirer, J.P. 1988. "Critical decisions under uncertainty: Representation and structure." Cognitive Science, 12, 177–210.

LaFrance, M. 1989. "The quality of expertise: Implications of expert-

novice differences for knowledge acquisition." SIGART Newsletter; 108(April):6–14.

Lakoff, G. 1987. Women, Fire, and Dangerous Things: What Categories Reveal About the Mind. Chicago: University of Chicago Press.

Mitchell, A.A. and Chi, M.T.H. 1984. "Measuring knowledge within a domain." Nagy, P (Ed.) The Representation of Cognitive Structures. Toronto: Ontario Institute for Studies in Education.

Reigeluth, C.M., Merrill, M.D., and Bunderson, C.V. 1994. "The structure of subject matter content and its instructional design implications." M.D. Merrill (Ed.), Instructional Design Theory. Englewood Cliffs, NJ: Educational Technology Publications, Inc. pp. 59–77.

Reimann, P. and Chi, M.T.H. 1989. "Human Expertise." K.J. Gilhooly (Ed.), Human and Machine Problem Solving (pp. 161–191). New York: Plenum Press.

Rosch, E. 1973. "Natural categories." Cognitive Psychology, 4, 328–50.

Spradley, J.P. 1979. The Ethnographic Interview. New York: Holt, Rinehart and Winston.

Werner, O. and Schoepfle, G.M. (Eds.). 1987. Systematic Fieldwork: Vol. 1. Foundations of Ethnography and Interviewing. Newbury Park, CA: Sage Publications.

Wixon, D., and Holtzblatt, K. 1990. "Contextual design: An emergent view of system design." Proceedings of CHI ‘90: Empowering People. Seattle, WA, ACM, pp. 329–336.

Wood, L.E., and Ford, J.M. 1993 “Structuring interviews with experts during knowledge elicitation." International Journal of Intelligent Systems: Special Issue on Knowledge Acquisition, 8, 71–90.

Wood. L.E. et al. 1995. "Evaluation of Interviewing Methods and Mediating Representations for Knowledge Acquisition." International Journal of Expert Systems: Research and Applications, 8(1), 1–23.

## EXAMPLE—INTERVIEW ANALYSIS AND WORK MODEL DEVELOPMENT

Given that the goal of interviews and observations regarding clients' work is to develop a work model, an analyst must obviously decide how to describe the model. As part of the work model description, I have found it helpful to construct object hierarchies to provide an organized summary view of the growing object structure. Given that the initial interviews are centered around Object Identification (see Table 4.1) and Object Relationship (see Table 4.2) questions, much of the analysis of the interview notes and tapes focuses on the extraction of that information and the construction of object hierarchies like that shown in Figure 3.1.

The development of a work model description (and the construction of object hierarchies in particular) is supported by a tool I have developed (to which I have referred elsewhere as a knowledge editor (Ford and Wood 1992)) that allows me to enter information about objects and their relationships to other objects. For example, an Object Relationship question asked of a client in the Telecom Services domain might be "What are the features of the fac/staff class of service?" The answer to that question would include a list of items such as conf(erence), intercom, long-distance, etc. as shown in Figure 3.1. The

![](images/581ee974b4cc873665d572f31d199e36f38e414dbbf58fc2e04f2c1de8417e55.jpg)  
FIGuRE 3.1 Part of the object hierarchy from the Telecom Services order project.

![](images/5d3efcf9ed736e416ac4c043005b407a5b544c96557de47c86e6dcba4c4a7f3b.jpg)  
FIGURE 3.2 Dialogue box for entering object information.

knowledge editor tool allows one to enter information relevant to those objects as shown in Figure 3.2.

Information regarding objects can be viewed and browsed as shown in Figure 3.3. At any point object hierarchies can be automatically generated, manipulated, and pasted into a work model description. The knowledge editor enables one to revise the object information and re-generate the object hierarchies relatively easily, especially compared to constructing and revising them with a general, or even specialized, drawing tool.

Currently, my work model descriptions are documents consisting of some beginning narrative describing the nature of the project, followed by linked object hierarchies, structured outlines describing process knowledge, an alphabetized object glossary with definitions, and other details about objects.

While work flow diagrams are helpful in showing the exchange of information among potential users and others in their work organization, I currently use structured outlines to represent detailed process knowledge in the work model descriptions. Structured outlines have several advantages. First, they provide a means of representing knowledge at the global, strategic level, while at the same time representing more specific knowledge within a particular structure as needed. Second, the structure of the outline can easily be modified to reflect changes in understanding that emerge from successive sessions with an expert.

![](images/8b87d1123abc36f5a52be525b8a5c62c8d1b8f5e80f405e2090fc534cf55d226.jpg)  
FIGURE 3.3 Display of information concerning an object and its relationships to other objects.

I have begun to experiment with flow charts, but they have the disadvantage of not being nearly as easy to modify and revise (i.e., I haven't devised a way to automatically generate them from a something akin to relationships among objects as with the object heirarchies). On the other hand, I have found evidence that experts using object heirarchies are faster, are more accurate, and much prefer graphical object hierarchies to outline versions (Wood et al. 1995).

I have found it convenient to document global segments of procedural information as it might emerge during object identification, and then to fill out details through analysis of later think-aloud protocols generated in the context of specific cases and examples of real work. For instance, in answer to the following Task-Related Grand Tour question (see Table 4.1)“Could you discuss the major steps you go through in filling a request for services from a member of your unit?", the following general outline of major steps in the generation of a Telecom Services request was generated:

receive request from a client

review/negotiate details

draft a description of the request

obtain authorized signatures and account #s

In later interviews, more detailed information regarding process knowledge was obtained, such as the segment shown in Figure 3.4.

<table><tr><td>Receive request from client (usually in the form on an e-mail message) Choose Use type If telephone Then Choose Need type If addition Then</td></tr><tr><td>Draw floor plan of the appropriate room</td></tr><tr><td>Specify current jack locations in room</td></tr><tr><td>If no jack exists at desired location Then specify jack installation at that location</td></tr><tr><td>Otherwise Determine jack numbers for existing jacks</td></tr><tr><td>Map extensions to new or existing jack (by number)</td></tr><tr><td>Select set type for new telephone(s)</td></tr><tr><td></td></tr><tr><td>Select face plate configuration from tables</td></tr><tr><td>Select line appearance</td></tr><tr><td>Review and select needed features</td></tr><tr><td>Draft a description for request</td></tr><tr><td></td></tr><tr><td>If change Then (see p. ?) for details)</td></tr><tr><td></td></tr></table>

FIGURE 3.4 A segment of a structured outline of Telecom Services order task.