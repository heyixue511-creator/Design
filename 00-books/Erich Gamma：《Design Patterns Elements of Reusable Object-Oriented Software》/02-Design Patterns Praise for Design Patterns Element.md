# Design Patterns

Elements of Reusable Object-Oriented Software

Erich Gamma

Richard Helm

Ralph Johnson

John Vlissides

六ADDISON-WESLEY

Boston • San Francisco • New York • Toronto • Montreal

London • Munich • Paris • Madrid

Capetown • Sidney • Tokyo • Singapore • Mexico City

Material from A Pattern Language: Towns/Buildings/Construction by Christopher Alexander, copyright © 1977 by Christopher Alexander is reprinted by permission of Oxford University Press, Inc.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and we were aware of a trademark claim, the designations have been printed in initial capital letters or in all capitals.

The author and publisher have taken care in the preparation of this book, but make no expressed or implied warranty of any kind and assume no responsibility for errors or omissions. No liability is assumed for incidental or consequential damages in connection with or arising out of the use of the information or programs contained herein.

The publisher offers discounts on this book when ordered in quantity for special sales. For more information, please contact:

Pearson Education Corporate Sales Division

201 W. 103rd Street

Indianapolis, IN 46290

(800) 428-5331

corpsales@pearsoned.com

Visit AW on the Web: www.awprofessional.com

Library of Congress Cataloging-in-Publication Data

Design Patterns : elements of reusable object-oriented software / Erich Gamma ... [et al.].

p. cm.—(Addison-Wesley professional computing series)

Includes bibliographical references and index.

ISBN 0-201-63361-2

1. Object-oriented programming (Computer science) 2. Computer software—Reusability.

I. Gamma, Erich. II. Series.

QA76.64.D47 1994

005.1'2—dc20

94-34264

CIP

Copyright © 1995 by Addison-Wesley

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form, or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior consent of the publisher. Printed in the United States of America. Published simultaneously in Canada.

Cover art © M.C. Escher/Cordon Art - Baarn - Holland. All rights reserved.

ISBN 0-201-63361-2

Text printed in the United States on recycled paper at Courier Westford in Westford, Massachusetts.

37th Printing March 2009

To Karin

—E.G.

To Sylvie

—R.H.

To Faith

—R.J.

To Dru Ann and Matthew Joshua 24:15b

—J.V.

## Praise for Design Patterns: Elements of Reusable Object-Oriented Software

“This is one of the best written and wonderfully insightful books that I have read in a great long while...this book establishes the legitimacy of patterns in the best way: not by argument but by example.”

## —Stan Lippman, C++ Report

“...this new book by Gamma, Helm, Johnson, and Vlissides promises to have an important and lasting impact on the discipline of software design. Because Design Patterns bills itself as being concerned with object-oriented software alone, I fear that software developers outside the object community may ignore it. This would be a shame. This book has something for everyone who designs software. All software designers use patterns; understanding better the reusable abstractions of our work can only make us better at it.”

## —Tom DeMarco, IEEE Software

“Overall, I think this book represents an extremely valuable and unique contribution to the field because it captures a wealth of object-oriented design experience in a compact and reusable form. This book is certainly one that I shall turn to often in search of powerful object-oriented design ideas; after all, that’s what reuse is all about, isn’t it?”

## —Sanjiv Gossain, Journal of Object-Oriented Programming

“This much-anticipated book lives up to its full year of advance buzz. The metaphor is of an architect’s pattern book filled with time-tested, usable designs. The authors have chosen 23 patterns from decades of object-oriented experience. The brilliance of the book lies in the discipline represented by that number. Give a copy of Design Patterns to every good programmer you know who wants to be better.”

## —Larry O’Brien, Software Development

“The simple fact of the matter is that patterns have the potential to permanently alter the software engineering field, catapulting it into the realm of true elegant design. Of the books to date on this subject, Design Patterns is far and away the best. It is a book to be read, studied, internalized, and loved. The book will forever change the way you view software.”

## —Steve Bilow, Journal of Object-Oriented Programming

“Design Patterns is a powerful book. After a modest investment of time with it, most C++ programmers will be able to start applying its “patterns” to produce better software. This book delivers intellectual leverage: concrete tools that help us think

and express ourselves more effectively. It may fundamentally change the way you think about programming.

—Tom Cargill, C++ Report