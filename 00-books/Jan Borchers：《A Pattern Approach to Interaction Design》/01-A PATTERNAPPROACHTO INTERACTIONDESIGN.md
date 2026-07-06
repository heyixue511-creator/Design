# A PATTERNAPPROACHTO INTERACTIONDESIGN

Jan Borchers Stanford University, USA

JOHN WILEY& SONS, LTD Chichester • Weinheim • New York • Brisbane • Singapore • Toronto

Copyright © 2001 by John Wiley & Sons Ltd Baffins Lane, Chichester, West Sussex, PO19 1UD, England

National 01243 779777   
International (+44) 1243 779777

e-mail (for orders and customer service enquiries): cs-books@wiley.co.uk

Visit our Home Page on http://www.wiley.co.uk

or

http://www.wiley.com

All Rights Reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, ın any form or by any means, electronic, mechanical, photocopying, recording, scanning or otherwise, except under the terms of the Copyright Designs and Patents Act 1988 or under the terms of a licence issued by the Copyright Licensing Agency, 90 Tottenham Court Road, London, W1P 9HE, UK, without the permission in writing of the Publisher, with the exception of any material supplied specifically for the purpose of being entered and executed on a computer system, for exclusive use by the purchaser of the publication.

Neither the authors nor John Wiley & Sons Ltd accept any responsibility or liability for loss or damage occasioned to any person or property through using the material, instructions, methods or ideas contained herein, or acting or refraining from acting as a result of such use. The authors and Publisher expressly disclaim all implied warranties, including merchantability of fitness for any particular purpose. There will be no duty on the authors of Publisher to correct any errors or defects in the software.

Designations used by companies to distinguish their products are often claimed as trademarks. In all instances where John Wiley & Sons is aware of a claim, the product names appear in initial capital or capital letters. Readers, however, should contact the appropriate companies for more complete information regarding trademarks and registration. Jan Borchers has asserted his right under the Copyright, Designs and Patents Act 1988 to be identified as the author of this work.

Other Wiley Editorial Offices

John Wiley & Sons, Inc., 605 Third Avenue, New York, NY 10158-0012, USA

Wiley-VCH Verlag GmbH Pappelallee 3, D-69469 Weinheim, Germany

John Wiley & Sons (Australia) Ltd, 33 Park Road, Milton, Queensland 4064, Australia

John Wiley & Sons (Canada) Ltd, 22 Worcester Road Rexdale, Ontario, M9W 1L1, Canada

John Wiley & Sons (Asia) Pte Ltd, 2 Clementi Loop #02-01, Jin Xing Distrıpark, Singapore 129809

Library of Congress Cataloging-in-Publication Data

Borchers, Jan A pattern approach to interactive design / Jan Borchers p. cm. (Wiley series in software design patterns) Includes bibliographical references and index ISBN 0 471 49828 9 1. Human-computer interaction. 2. Computer software - Development. I. Title II. Series QA76.9. H85 B67 2001 004' 01'9-dc21 00-054570

British Library Cataloguing in Publication Data

A catalogue record for this book is available from the British Library

ISBN 0 471 49828 9

Typeset in Palatino by the author using LaTeX software Printed and bound in Great Britain by Biddles Ltd, Guildford and King's Lynn. This book is printed on acid-free paper responsibly manufactured from sustainable forestry, for which at least two trees are planted for each one used for paper production.

## Contents

Preface xi   
Series Foreword xiii   
Acknowledgements xvii   
1 Introduction 1   
1.1 Why User Interfaces Matter 1   
1.2 Interdisciplinary Design and Its Problems . . 3   
1.3 Capturing Experience 5   
1.4 A Pattern Framework. 6   
1.5 How This Book Is Organized 7   
2Design Pattern Languages 9   
2.1Pattern Languages in Architecture 9   
2.2 Pattern Languages in Software Engineering.22   
2.3 Pattern Languages in HCI. 26   
2.4Pattern Languages in Other Disciplines 43   
2.5 A Comparison of Central Pattern Collections 46   
2.6Pattern Language Framework Requirements 47   
3 An Interdisciplinary Pattern Framework 51   
3.1 A Formal Model of Pattern Languages . . . 52   
3.2 Pattern Languages in the Software Lifecycle . 54   
3.2.1 The Usability Engineering Lifecycle. 57   
3.2.2 The Pattern Framework in the Lifecyle 58   
3.3 Time in Patterns 63   
3.4 Patterns and Their Components in Detail 64   
3.4.1 Name 65   
3.4.2 Ranking 66   
3.4.3 Illustration 66   
3.4.4 Problem and Forces 68   
3.4.5 Examples 69   
3.4.6 Solution 70   
3.4.7 Diagram 71   
3.4.8 Context and References 71   
4 A Pattern Language for Interactive Music Exhibits75   
4.1 Musical Pattern Language 78   
M1 BLUES STYLE 81   
M2 COMBO INSTRUMENTATION 83   
M3 SOLO & COMPING \* 85   
M4 TWELVE-BAR PROGRESSION 87   
M5 SIXTH AND SEVENTH CHORDS 89   
M6 CHORD TRANSITIONS 91   
M7 PENTATONIC SCALE \*\* 93   
M8 BLUE NOTES\*\* 95   
M9 TRIPLET GROOVE \*\* 97   
M10 WALKING BASS \* 99   
M11 BLUES TEMPO 101   
4.2 HCI Pattern Language 102   
H1 ATTRACT-ENGAGE-DELIVER\* . 105   
H2 ATTRACTION SPACE \* .109   
H3 COOPERATIVE EXPERIENCE \*\* . 113   
H4 EASY HANDOVER \* 117   
H5 SIMPLE IMPRESSION\* .120   
H6 INCREMENTAL REVEALING\*\* . . 122   
H7 FLAT AND NARROW TREE \* . . 124   
H8 AUGMENTED REALITY \* . 126   
H9 CLOSED LOOP \* . 129   
H10 LANGUAGE INDEPENDENCE . 131   
H11 DOMAIN-APPROPRIATE DEVICES \*. . 133   
H12 INNOVATIVE APPEARANCE\* .. 137   
H13 IMMERSIVE DISPLAY \* 139   
H14 INVISIBLE HARDWARE\* 141   
H15 DYNAMIC DESCRIPTOR\*\* 144   
H16 INFORMATION JUST IN TIME \*\* . 147   
H17 ONE INPUT DEVICE \* . 149   
4.3 Software Pattern Language . 152   
S1 BRANCHING TRANSFORMER CHAIN. 153   
S2 METRIC TRANSFORMER\*. . . . 156   
S3 IMPROVISATION HELPER\*\* .161   
S4 MUSICAL EVENTS \* .166   
5 Evaluation and Tool Support 169   
5.1 Comparison With Framework Requirements 170   
5.2Pattern Peer Review 171   
5.2.1 Summary 176   
5.2.2 Positive Formal Aspects. . 176   
5.2.3 Positive Contents Aspects . . . . . . . 177   
5.2.4 Format Improvement Suggestions . . 177   
5.2.5 Contents Improvement Suggestions . 178   
5.2.6 Conclusion: Main Advantages . . . . 179   
5.3 Comparison With CHI 2000 Workshop Results 179   
5.4Evaluation of a Resulting System: WorldBeat 180   
5.4.1 Project Background . . . 181   
5.4.2System Features . 182   
5.4.3 Implementation. 183   
5.4.4 Usage Scenario 185   
5.4.5Evaluation 187   
5.5Reusing Patterns 189   
5.5.1 The Interactive Fugue 189   
5.5.2 Personal Orchestra and Virtual Vienna . 191   
5.6Study of Didactic Usefulness . 193   
5.7 Publishing Peer Review. . 195   
5.8PET: A Pattern EditingTool. 195   
6 Summary and Further Research 203   
6.1 Motivation 203   
6.2 Main Contributions. . 204   
6.3Further Research 206   
Bibliography 209   
A Online Resources 219   
BWorldBeat Sample Run 221   
B.1 WorldBeat: Interacting With Music . . . . . . 221   
B.2 Scenario: A Screen, And Two Batons. . . . . 221   
B.3 Start Page: Entering the Exhibit . . . . . . . . 222   
B.4Choosing From Six Components . . . . . . . 222   
B.5 Virtual Baton . . 223   
B.6 Joy-Sticks. . 223   
B.7Musical Memory . 224   
B.8Query By Humming 224   
B.9Musical Design Patterns 225   
B.10NetMusic. 226   
B.11Leaving the Exhibit. 226   
List of Figures and Credits 233   
Index 239

This Page Intentionally Left Blank

## Preface

Designing successful interactive systems requires user interface designers to work together with software engineers and application domain experts in an interdisciplinary team. A major problemwithin suchgroups is communicationbetween team members. Patternlanguageshave beencommunicatingdesign knowledge successfully within architecture andsoftware engineering in the past. This book summarizes the state of pattern languages in human-computer interaction (HCI), andproposes a new pattern-based frameworkfor interactive systems design. It extends the pattern idea to a uniform model for expressing design issues of HCI, software engineering, and application domain of a project.

As an example, the framework is appliedto describe design issues for interactive exhibits and similar public “kiosk" systems. The patterns were drawn from the author's design experience from a number of such systems, starting with the World-Beat project, in which an award-winning interactive music exhibit was developed. WorldBeat lets users interact with musical concepts in entirely new ways, from playing virtual drums, to finding tunes by humming, to improvising to a blues band without playing incorrectly, using just a pair of infrared batons. The patterns were then used and refined in the design of subsequent interactive exhibits, including the Interactive Fugue about classical music, the Personal Orchestra system to virtually conduct the Vienna Philharmonic,and the Virtual Vienna 3-D city tour.

The result is a comprehensive pattern language about user interface design for interactive exhibits and public systems. Also shown is the pattern language describing concepts of the application domain “music"in the original WorldBeat system, and several patterns of successful software engineering solutions in those systems. Finally, the design of a software tool to work with pattern languages is presented.

It is shown how the pattern-based framework improves communication within design teams, and helps creating a design rationale and corporate memory of design experience for follow-up projects, new team members, and teaching.

For updates to this book, and current information about HCI Design Patterns, please visit the HCI Patterns Home Page at http://www.hcipatterns.org/.

This Page Intentionally Left Blank