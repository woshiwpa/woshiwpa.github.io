# this script should be run in Linux/Cygwin. Its path and Url are all divided by forward slash.
import os
import shutil

sourceWebPagesFolder = 'D:/Development/git_repo/MFPLang4JVM/docs'
destWebPagesFolder = 'D:/Development/git_repo/woshiwpa.github.io/MFPLang'

styleStr = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: "Lato", sans-serif;
}

.sidenav {
  height: 100%;
  width: 200px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  /*font-size: 16px;*/
  color: #818181;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.main {
  margin-left: 200px; /* Same as the width of the sidenav */
  /*font-size: 28px;  Increased text to enable scrolling */
  padding: 0px 10px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
'''
endOfFileStr = '''</div>
   
</body>
</html>'''

class MFPWebSiteNode:
    def __init__(self, name: str, pageFilePath: str, parent):
        self.name = name
        self.pageFilePath = pageFilePath
        self.parent = parent
        self.children = []
        if parent is not None:
            # hook itself to parent.
            parent.__addChild(self)
            self.level = parent.level + 1
        else:
            self.level = 0
        self.upperLevelStr = ''.join(['../' for idx in range(self.pageFilePath.count('/'))])
        fontStr = '<p style="font-size:{0}px;">'.format(18 - 3*self.level)
        self.myLine = '\t' + fontStr + '<a href="' + self.pageFilePath + '">' + self.name + '</a></p>\n'
    
    def __addChild(self, childNode):
        self.children.append(childNode)
        
    def outputSideBar(webpageNode, lang):
        otherLang = 'en' if lang != 'en' else 'zh-CN'
        otherLangRefStr = '<p style="font-size:18px;"><a href="../' + otherLang + '/MFPIndex.html">' + ('[English Version]' if otherLang == 'en' else '???????????????') + '</a></p>\n'
        totalLines = webpageNode.myLine
        for child in webpageNode.children:
            totalLines += child.myLine

        thisLevelNode = webpageNode
        thisParentNode = webpageNode.parent
        while thisParentNode is not None:
            totalLinesOld = totalLines
            totalLines = ''
            for child in thisParentNode.children:
                if child == thisLevelNode:
                    childLine = totalLinesOld
                else:
                    childLine = child.myLine
                totalLines += childLine
            totalLines = thisParentNode.myLine + totalLines
            thisLevelNode = thisParentNode
            thisParentNode = thisLevelNode.parent
        totalLines += '<p/><p/><p/>' # add 3 more lines to avoid x-scrolling bar covers sidebar items.
        return otherLangRefStr + totalLines
                
for lang in ['en', 'zh-CN']:
    if os.path.exists(destWebPagesFolder + '/' + lang + '/'):
        shutil.rmtree(destWebPagesFolder + '/' + lang + '/')
    shutil.copytree(sourceWebPagesFolder + '/' + lang + '/', destWebPagesFolder + '/' + lang + '/')

    indexName = 'Introduction' if lang != 'zh-CN' else 'MFP?????????????????????????????????'

    languageName = 'MFP language introduction' if lang != 'zh-CN' else 'MFP????????????'
    operatorsName = 'operators'
    functionStatementName = 'function'
    variableStatementName = 'variable'
    ifStatementName = 'if'
    loopStatementName = 'while do for'
    breakStatementName = 'break continue'
    selectStatementName = 'select'
    tryStatementName = 'try catch'
    classStatementName = 'class'
    callStatementName = 'call'
    citingspaceStatementName = 'citingspace'
    helpStatementName = 'help'
    compulsoryLinkAnnotationName = '@compulsory_link'
    executionEntryAnnotationName = '@execution_entry'
    buildAssetAnnotationName = '@build_asset'

    functionIndexName = 'MFP functions' if lang != 'zh-CN' else 'MFP??????'
    allFunctionsName = 'all functions' if lang != 'zh-CN' else '????????????'
    integerFunctionsName = 'integer operation' if lang != 'zh-CN' else '??????????????????'
    logicFunctionsName = 'logic functions' if lang != 'zh-CN' else '????????????'
    statisticFunctionsName = 'statistic and stochastic' if lang != 'zh-CN' else '?????????????????????'
    trigononmetricFunctionsName = 'trigononmetric functions' if lang != 'zh-CN' else '????????????'
    exponentialFunctionsName = 'exponential functions' if lang != 'zh-CN' else '????????????'
    complexFunctionsName = 'complex number' if lang != 'zh-CN' else '????????????'
    systemFunctionsName = 'system functions' if lang != 'zh-CN' else '????????????'
    arrayFunctionsName = 'array or matrix' if lang != 'zh-CN' else '?????????????????????'
    graphicFunctionsName = 'graphic functions' if lang != 'zh-CN' else '????????????'
    expressionFunctionsName = 'expression and calculus' if lang != 'zh-CN' else '???????????????????????????'
    stringFunctionsName = 'string functions' if lang != 'zh-CN' else '???????????????'
    hyperbolicFunctionsName = 'hyperbolic trigononmetric' if lang != 'zh-CN' else '??????????????????'
    sortingFunctionsName = 'sorting functions' if lang != 'zh-CN' else '????????????'
    polynomialFunctionsName = 'polynomial' if lang != 'zh-CN' else '???????????????'
    signalFunctionsName = 'signal processing' if lang != 'zh-CN' else '??????????????????'
    fileFunctionsName = 'file operation' if lang != 'zh-CN' else '??????????????????'
    timedateFunctionsName = 'time and date' if lang != 'zh-CN' else '?????????????????????'
    displayFunctionsName = 'graphic display' if lang != 'zh-CN' else '????????????'
    multimediaFunctionsName = 'multimedia functions' if lang != 'zh-CN' else '???????????????'
    datastructureFunctionsName = 'data structure' if lang != 'zh-CN' else '??????????????????'
    platformFunctionsName = 'platform and hardware' if lang != 'zh-CN' else '?????????????????????'
    parallelFunctionsName = 'parallel computing' if lang != 'zh-CN' else '??????????????????'
    reflectionFunctionsName = 'reflection' if lang != 'zh-CN' else '????????????'
    mfpcompilingFunctionsName = 'MFP compiling' if lang != 'zh-CN' else 'MFP????????????'
    othersFunctionsName = 'others' if lang != 'zh-CN' else '????????????'

    buildAPKTopicName = 'build Android APK' if lang != 'zh-CN' else '?????????????????????'

    gameTopicName = 'game programming' if lang != 'zh-CN' else '??????????????????'
    gameFundamentalTopicName = 'game fundametnal' if lang != 'zh-CN' else '???????????????'
    hungrysnakeTopicName = 'a hungry snake game' if lang != 'zh-CN' else '?????????????????????'
    gemcrushTopicName = 'a gem crush game' if lang != 'zh-CN' else '?????????????????????'
    rabbitjumpingTopicName = 'a rabbit jumping game' if lang != 'zh-CN' else '???????????????????????????'
    multiplayerTopicName = 'multiple device/player game' if lang != 'zh-CN' else '????????????????????????'

    chartingTopicName = 'chart plotting' if lang != 'zh-CN' else '????????????'
    #chartfunctionsTopicName = 'chart plotting functions' if lang != 'zh-CN' else '??????????????????'
    #charttoolsTopicName = 'chart plotting tools' if lang != 'zh-CN' else '??????????????????'



    # Now build side bar list. Note that the address is always forward slash
    allNodes = set()
    websiteRootNode = MFPWebSiteNode(indexName, 'MFPIndex.html', None)
    allNodes.add(websiteRootNode)
    languageNode = MFPWebSiteNode(languageName, 'LanguageInfo/language.html', websiteRootNode)
    allNodes.add(languageNode)
    functionIndexNode = MFPWebSiteNode(functionIndexName, 'FunctionInfo/functions.html', websiteRootNode)
    allNodes.add(functionIndexNode)
    buildAPKTopicNode = MFPWebSiteNode(buildAPKTopicName, 'HowtoInfo/build_apk.html', websiteRootNode)
    allNodes.add(buildAPKTopicNode)
    gameTopicNode = MFPWebSiteNode(gameTopicName, 'GameProgramming/index.html', websiteRootNode)
    allNodes.add(gameTopicNode)
    chartingTopicNode = MFPWebSiteNode(chartingTopicName, 'ChartPlotting/index.html', websiteRootNode)
    allNodes.add(chartingTopicNode)

    operatorsNode = MFPWebSiteNode(operatorsName, 'LanguageInfo/operators.html', languageNode)
    allNodes.add(operatorsNode)
    functionStatementNode = MFPWebSiteNode(functionStatementName, 'LanguageInfo/function_return_endf.html', languageNode)
    allNodes.add(functionStatementNode)
    variableStatementNode = MFPWebSiteNode(variableStatementName, 'LanguageInfo/variable.html', languageNode)
    allNodes.add(variableStatementNode)
    ifStatementNode = MFPWebSiteNode(ifStatementName, 'LanguageInfo/if_elseif_else_endif.html', languageNode)
    allNodes.add(ifStatementNode)
    loopStatementNode = MFPWebSiteNode(loopStatementName, 'LanguageInfo/while_loop_do_until_for_next.html', languageNode)
    allNodes.add(loopStatementNode)
    breakStatementNode = MFPWebSiteNode(breakStatementName, 'LanguageInfo/break_continue.html', languageNode)
    allNodes.add(breakStatementNode)
    selectStatementNode = MFPWebSiteNode(selectStatementName, 'LanguageInfo/select_case_default_ends.html', languageNode)
    allNodes.add(selectStatementNode)
    tryStatementNode = MFPWebSiteNode(tryStatementName, 'LanguageInfo/try_throw_catch_endtry.html', languageNode)
    allNodes.add(tryStatementNode)
    classStatementNode = MFPWebSiteNode(classStatementName, 'LanguageInfo/class_endclass.html', languageNode)
    allNodes.add(classStatementNode)
    callStatementNode = MFPWebSiteNode(callStatementName, 'LanguageInfo/call_endcall.html', languageNode)
    allNodes.add(callStatementNode)
    citingspaceStatementNode = MFPWebSiteNode(citingspaceStatementName, 'LanguageInfo/citingspace_using.html', languageNode)
    allNodes.add(citingspaceStatementNode)
    helpStatementNode = MFPWebSiteNode(helpStatementName, 'LanguageInfo/help_endh_ATlanguage.html', languageNode)
    allNodes.add(helpStatementNode)
    compulsoryLinkAnnotationNode = MFPWebSiteNode(compulsoryLinkAnnotationName, 'LanguageInfo/ATcompulsory_link.html', languageNode)
    allNodes.add(compulsoryLinkAnnotationNode)
    executionEntryAnnotationNode = MFPWebSiteNode(executionEntryAnnotationName, 'LanguageInfo/ATexecution_entry.html', languageNode)
    allNodes.add(executionEntryAnnotationNode)
    buildAssetAnnotationNode = MFPWebSiteNode(buildAssetAnnotationName, 'LanguageInfo/ATbuild_asset.html', languageNode)
    allNodes.add(buildAssetAnnotationNode)

    allFunctionsNode = MFPWebSiteNode(allFunctionsName, 'FunctionInfo/all.html', functionIndexNode)
    allNodes.add(allFunctionsNode)
    integerFunctionsNode = MFPWebSiteNode(integerFunctionsName, 'FunctionInfo/integer_operation.html', functionIndexNode)
    allNodes.add(integerFunctionsNode)
    logicFunctionsNode = MFPWebSiteNode(logicFunctionsName, 'FunctionInfo/logic.html', functionIndexNode)
    allNodes.add(logicFunctionsNode)
    statisticFunctionsNode = MFPWebSiteNode(statisticFunctionsName, 'FunctionInfo/statistic_and_stochastic.html', functionIndexNode)
    allNodes.add(statisticFunctionsNode)
    trigononmetricFunctionsNode = MFPWebSiteNode(trigononmetricFunctionsName, 'FunctionInfo/trigononmetric.html', functionIndexNode)
    allNodes.add(trigononmetricFunctionsNode)
    exponentialFunctionsNode = MFPWebSiteNode(exponentialFunctionsName, 'FunctionInfo/exponential_and_logarithmic.html', functionIndexNode)
    allNodes.add(exponentialFunctionsNode)
    complexFunctionsNode = MFPWebSiteNode(complexFunctionsName, 'FunctionInfo/complex_number.html', functionIndexNode)
    allNodes.add(complexFunctionsNode)
    systemFunctionsNode = MFPWebSiteNode(systemFunctionsName, 'FunctionInfo/system.html', functionIndexNode)
    allNodes.add(systemFunctionsNode)
    arrayFunctionsNode = MFPWebSiteNode(arrayFunctionsName, 'FunctionInfo/array_or_matrix.html', functionIndexNode)
    allNodes.add(arrayFunctionsNode)
    graphicFunctionsNode = MFPWebSiteNode(graphicFunctionsName, 'FunctionInfo/graphic.html', functionIndexNode)
    allNodes.add(graphicFunctionsNode)
    expressionFunctionsNode = MFPWebSiteNode(expressionFunctionsName, 'FunctionInfo/expression_and_calculus.html', functionIndexNode)
    allNodes.add(expressionFunctionsNode)
    stringFunctionsNode = MFPWebSiteNode(stringFunctionsName, 'FunctionInfo/string.html', functionIndexNode)
    allNodes.add(stringFunctionsNode)
    hyperbolicFunctionsNode = MFPWebSiteNode(hyperbolicFunctionsName, 'FunctionInfo/hyperbolic_trigononmetric.html', functionIndexNode)
    allNodes.add(hyperbolicFunctionsNode)
    sortingFunctionsNode = MFPWebSiteNode(sortingFunctionsName, 'FunctionInfo/sorting.html', functionIndexNode)
    allNodes.add(sortingFunctionsNode)
    polynomialFunctionsNode = MFPWebSiteNode(polynomialFunctionsName, 'FunctionInfo/polynomial.html', functionIndexNode)
    allNodes.add(polynomialFunctionsNode)
    signalFunctionsNode = MFPWebSiteNode(signalFunctionsName, 'FunctionInfo/signal_proc.html', functionIndexNode)
    allNodes.add(signalFunctionsNode)
    fileFunctionsNode = MFPWebSiteNode(fileFunctionsName, 'FunctionInfo/file.html', functionIndexNode)
    allNodes.add(fileFunctionsNode)
    timedateFunctionsNode = MFPWebSiteNode(timedateFunctionsName, 'FunctionInfo/time_and_date.html', functionIndexNode)
    allNodes.add(timedateFunctionsNode)
    displayFunctionsNode = MFPWebSiteNode(displayFunctionsName, 'FunctionInfo/gdi.html', functionIndexNode)
    allNodes.add(displayFunctionsNode)
    multimediaFunctionsNode = MFPWebSiteNode(multimediaFunctionsName, 'FunctionInfo/multimedia.html', functionIndexNode)
    allNodes.add(multimediaFunctionsNode)
    datastructureFunctionsNode = MFPWebSiteNode(datastructureFunctionsName, 'FunctionInfo/datastruct.html', functionIndexNode)
    allNodes.add(datastructureFunctionsNode)
    platformFunctionsNode = MFPWebSiteNode(platformFunctionsName, 'FunctionInfo/platform_hardware.html', functionIndexNode)
    allNodes.add(platformFunctionsNode)
    parallelFunctionsNode = MFPWebSiteNode(parallelFunctionsName, 'FunctionInfo/parallel.html', functionIndexNode)
    allNodes.add(parallelFunctionsNode)
    reflectionFunctionsNode = MFPWebSiteNode(reflectionFunctionsName, 'FunctionInfo/reflection.html', functionIndexNode)
    allNodes.add(reflectionFunctionsNode)
    mfpcompilingFunctionsNode = MFPWebSiteNode(mfpcompilingFunctionsName, 'FunctionInfo/mfpcompiler.html', functionIndexNode)
    allNodes.add(mfpcompilingFunctionsNode)
    othersFunctionsNode = MFPWebSiteNode(othersFunctionsName, 'FunctionInfo/others.html', functionIndexNode)
    allNodes.add(othersFunctionsNode)

    gameFundamentalTopicNode = MFPWebSiteNode(gameFundamentalTopicName, 'GameProgramming/game_fundamental.html', gameTopicNode)
    allNodes.add(gameFundamentalTopicNode)
    hungrysnakeTopicNode = MFPWebSiteNode(hungrysnakeTopicName, 'GameProgramming/hungry_snake.html', gameTopicNode)
    allNodes.add(hungrysnakeTopicNode)
    gemcrushTopicNode = MFPWebSiteNode(gemcrushTopicName, 'GameProgramming/gem_gem.html', gameTopicNode)
    allNodes.add(gemcrushTopicNode)
    rabbitjumpingTopicNode = MFPWebSiteNode(rabbitjumpingTopicName, 'GameProgramming/super_rabbit.html', gameTopicNode)
    allNodes.add(rabbitjumpingTopicNode)
    multiplayerTopicNode = MFPWebSiteNode(multiplayerTopicName, 'GameProgramming/multi_player_hungry_snake.html', gameTopicNode)
    allNodes.add(multiplayerTopicNode)

    for webpageNode in allNodes:
        sideBarStr = '</head>\n<body>\n\n<div class="sidenav">\n'+ MFPWebSiteNode.outputSideBar(webpageNode, lang) + '</div>\n\n<div class="main">\n'

        titleStr = ''
        bodyStrStart = False
        bodyStr = ''
        with open(sourceWebPagesFolder + '/' + lang + '/' + webpageNode.pageFilePath, 'r') as f:
            for line in f:
                lineNoBlank = line.lstrip().lower()
                # For each line, check if line contains the string
                if lineNoBlank.startswith('<title>') and ('</title>' in lineNoBlank):
                    titleStr = line
                if (not bodyStrStart) and lineNoBlank.startswith('<body style="background-color:white;">'):
                    bodyStrStart = True
                elif bodyStrStart:
                    if lineNoBlank.startswith('</body>'):
                        bodyStrStart = False
                    else:
                        bodyStr += line
                
        fullTextStr = styleStr + titleStr + sideBarStr.replace('<a href="', '<a href="' + webpageNode.upperLevelStr) + bodyStr + endOfFileStr
        with open(destWebPagesFolder + '/' + lang + '/' + webpageNode.pageFilePath, 'w') as f:
            f.write(fullTextStr)
            
            
