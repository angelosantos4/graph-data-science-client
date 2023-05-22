EXAMPLE_SERVER_ENDPOINTS = [
    "gds.allShortestPaths.delta.mutate",
    "gds.allShortestPaths.delta.mutate.estimate",
    "gds.allShortestPaths.delta.stats",
    "gds.allShortestPaths.delta.stats.estimate",
    "gds.allShortestPaths.delta.stream",
    "gds.allShortestPaths.delta.stream.estimate",
    "gds.allShortestPaths.delta.write",
    "gds.allShortestPaths.delta.write.estimate",
    "gds.allShortestPaths.dijkstra.mutate",
    "gds.allShortestPaths.dijkstra.mutate.estimate",
    "gds.allShortestPaths.dijkstra.stream",
    "gds.allShortestPaths.dijkstra.stream.estimate",
    "gds.allShortestPaths.dijkstra.write",
    "gds.allShortestPaths.dijkstra.write.estimate",
    "gds.alpha.allShortestPaths.stream",
    "gds.alpha.backup",
    "gds.alpha.closeness.harmonic.stream",
    "gds.alpha.closeness.harmonic.write",
    "gds.alpha.conductance.stream",
    "gds.alpha.config.defaults.list",
    "gds.alpha.config.defaults.set",
    "gds.alpha.config.limits.list",
    "gds.alpha.config.limits.set",
    "gds.alpha.create.cypherdb",
    "gds.alpha.graph.graphProperty.drop",
    "gds.alpha.graph.graphProperty.stream",
    "gds.alpha.graph.nodeLabel.mutate",
    "gds.alpha.graph.nodeLabel.write",
    "gds.alpha.hits.mutate",
    "gds.alpha.hits.mutate.estimate",
    "gds.alpha.hits.stats",
    "gds.alpha.hits.stats.estimate",
    "gds.alpha.hits.stream",
    "gds.alpha.hits.stream.estimate",
    "gds.alpha.hits.write",
    "gds.alpha.hits.write.estimate",
    "gds.alpha.kSpanningTree.write",
    "gds.alpha.knn.filtered.mutate",
    "gds.alpha.knn.filtered.stats",
    "gds.alpha.knn.filtered.stream",
    "gds.alpha.knn.filtered.write",
    "gds.alpha.maxkcut.mutate",
    "gds.alpha.maxkcut.mutate.estimate",
    "gds.alpha.maxkcut.stream",
    "gds.alpha.maxkcut.stream.estimate",
    "gds.alpha.ml.splitRelationships.mutate",
    "gds.alpha.model.delete",
    "gds.alpha.model.load",
    "gds.alpha.model.publish",
    "gds.alpha.model.store",
    "gds.alpha.modularity.stats",
    "gds.alpha.modularity.stream",
    "gds.alpha.nodeSimilarity.filtered.mutate",
    "gds.alpha.nodeSimilarity.filtered.mutate.estimate",
    "gds.alpha.nodeSimilarity.filtered.stats",
    "gds.alpha.nodeSimilarity.filtered.stats.estimate",
    "gds.alpha.nodeSimilarity.filtered.stream",
    "gds.alpha.nodeSimilarity.filtered.stream.estimate",
    "gds.alpha.nodeSimilarity.filtered.write",
    "gds.alpha.nodeSimilarity.filtered.write.estimate",
    "gds.alpha.pipeline.linkPrediction.addMLP",
    "gds.alpha.pipeline.linkPrediction.addRandomForest",
    "gds.alpha.pipeline.linkPrediction.configureAutoTuning",
    "gds.alpha.pipeline.nodeClassification.addMLP",
    "gds.alpha.pipeline.nodeClassification.addRandomForest",
    "gds.alpha.pipeline.nodeClassification.configureAutoTuning",
    "gds.alpha.pipeline.nodeRegression.addLinearRegression",
    "gds.alpha.pipeline.nodeRegression.addNodeProperty",
    "gds.alpha.pipeline.nodeRegression.addRandomForest",
    "gds.alpha.pipeline.nodeRegression.configureAutoTuning",
    "gds.alpha.pipeline.nodeRegression.configureSplit",
    "gds.alpha.pipeline.nodeRegression.create",
    "gds.alpha.pipeline.nodeRegression.predict.mutate",
    "gds.alpha.pipeline.nodeRegression.predict.stream",
    "gds.alpha.pipeline.nodeRegression.selectFeatures",
    "gds.alpha.pipeline.nodeRegression.train",
    "gds.alpha.restore",
    "gds.alpha.scaleProperties.mutate",
    "gds.alpha.scaleProperties.stream",
    "gds.alpha.scc.stream",
    "gds.alpha.scc.write",
    "gds.alpha.sllpa.mutate",
    "gds.alpha.sllpa.mutate.estimate",
    "gds.alpha.sllpa.stats",
    "gds.alpha.sllpa.stats.estimate",
    "gds.alpha.sllpa.stream",
    "gds.alpha.sllpa.stream.estimate",
    "gds.alpha.sllpa.write",
    "gds.alpha.sllpa.write.estimate",
    "gds.alpha.systemMonitor",
    "gds.alpha.triangles",
    "gds.alpha.userLog",
    "gds.articleRank.mutate",
    "gds.articleRank.mutate.estimate",
    "gds.articleRank.stats",
    "gds.articleRank.stats.estimate",
    "gds.articleRank.stream",
    "gds.articleRank.stream.estimate",
    "gds.articleRank.write",
    "gds.articleRank.write.estimate",
    "gds.beta.closeness.mutate",
    "gds.beta.closeness.stats",
    "gds.beta.closeness.stream",
    "gds.beta.closeness.write",
    "gds.beta.collapsePath.mutate",
    "gds.beta.graph.export.csv",
    "gds.beta.graph.export.csv.estimate",
    "gds.beta.graph.generate",
    "gds.beta.graph.project.subgraph",
    "gds.beta.graph.relationships.stream",
    "gds.beta.graph.relationships.toUndirected",
    "gds.beta.graph.relationships.toUndirected.estimate",
    "gds.beta.graphSage.mutate",
    "gds.beta.graphSage.mutate.estimate",
    "gds.beta.graphSage.stream",
    "gds.beta.graphSage.stream.estimate",
    "gds.beta.graphSage.train",
    "gds.beta.graphSage.train.estimate",
    "gds.beta.graphSage.write",
    "gds.beta.graphSage.write.estimate",
    "gds.beta.hashgnn.mutate",
    "gds.beta.hashgnn.mutate.estimate",
    "gds.beta.hashgnn.stream",
    "gds.beta.hashgnn.stream.estimate",
    "gds.beta.influenceMaximization.celf.mutate",
    "gds.beta.influenceMaximization.celf.mutate.estimate",
    "gds.beta.influenceMaximization.celf.stats",
    "gds.beta.influenceMaximization.celf.stats.estimate",
    "gds.beta.influenceMaximization.celf.stream",
    "gds.beta.influenceMaximization.celf.stream.estimate",
    "gds.beta.influenceMaximization.celf.write",
    "gds.beta.influenceMaximization.celf.write.estimate",
    "gds.beta.k1coloring.mutate",
    "gds.beta.k1coloring.mutate.estimate",
    "gds.beta.k1coloring.stats",
    "gds.beta.k1coloring.stats.estimate",
    "gds.beta.k1coloring.stream",
    "gds.beta.k1coloring.stream.estimate",
    "gds.beta.k1coloring.write",
    "gds.beta.k1coloring.write.estimate",
    "gds.beta.kmeans.mutate",
    "gds.beta.kmeans.mutate.estimate",
    "gds.beta.kmeans.stats",
    "gds.beta.kmeans.stats.estimate",
    "gds.beta.kmeans.stream",
    "gds.beta.kmeans.stream.estimate",
    "gds.beta.kmeans.write",
    "gds.beta.kmeans.write.estimate",
    "gds.beta.leiden.mutate",
    "gds.beta.leiden.mutate.estimate",
    "gds.beta.leiden.stats",
    "gds.beta.leiden.stats.estimate",
    "gds.beta.leiden.stream",
    "gds.beta.leiden.stream.estimate",
    "gds.beta.leiden.write",
    "gds.beta.leiden.write.estimate",
    "gds.beta.listProgress",
    "gds.beta.model.drop",
    "gds.beta.model.exists",
    "gds.beta.model.list",
    "gds.beta.modularityOptimization.mutate",
    "gds.beta.modularityOptimization.mutate.estimate",
    "gds.beta.modularityOptimization.stream",
    "gds.beta.modularityOptimization.stream.estimate",
    "gds.beta.modularityOptimization.write",
    "gds.beta.modularityOptimization.write.estimate",
    "gds.beta.node2vec.mutate",
    "gds.beta.node2vec.mutate.estimate",
    "gds.beta.node2vec.stream",
    "gds.beta.node2vec.stream.estimate",
    "gds.beta.node2vec.write",
    "gds.beta.node2vec.write.estimate",
    "gds.beta.pipeline.drop",
    "gds.beta.pipeline.exists",
    "gds.beta.pipeline.linkPrediction.addFeature",
    "gds.beta.pipeline.linkPrediction.addLogisticRegression",
    "gds.beta.pipeline.linkPrediction.addNodeProperty",
    "gds.beta.pipeline.linkPrediction.configureSplit",
    "gds.beta.pipeline.linkPrediction.create",
    "gds.beta.pipeline.linkPrediction.predict.mutate",
    "gds.beta.pipeline.linkPrediction.predict.mutate.estimate",
    "gds.beta.pipeline.linkPrediction.predict.stream",
    "gds.beta.pipeline.linkPrediction.predict.stream.estimate",
    "gds.beta.pipeline.linkPrediction.train",
    "gds.beta.pipeline.linkPrediction.train.estimate",
    "gds.beta.pipeline.list",
    "gds.beta.pipeline.nodeClassification.addLogisticRegression",
    "gds.beta.pipeline.nodeClassification.addNodeProperty",
    "gds.beta.pipeline.nodeClassification.configureSplit",
    "gds.beta.pipeline.nodeClassification.create",
    "gds.beta.pipeline.nodeClassification.predict.mutate",
    "gds.beta.pipeline.nodeClassification.predict.mutate.estimate",
    "gds.beta.pipeline.nodeClassification.predict.stream",
    "gds.beta.pipeline.nodeClassification.predict.stream.estimate",
    "gds.beta.pipeline.nodeClassification.predict.write",
    "gds.beta.pipeline.nodeClassification.predict.write.estimate",
    "gds.beta.pipeline.nodeClassification.selectFeatures",
    "gds.beta.pipeline.nodeClassification.train",
    "gds.beta.pipeline.nodeClassification.train.estimate",
    "gds.beta.spanningTree.mutate",
    "gds.beta.spanningTree.mutate.estimate",
    "gds.beta.spanningTree.stats",
    "gds.beta.spanningTree.stats.estimate",
    "gds.beta.spanningTree.stream",
    "gds.beta.spanningTree.stream.estimate",
    "gds.beta.spanningTree.write",
    "gds.beta.spanningTree.write.estimate",
    "gds.beta.steinerTree.mutate",
    "gds.beta.steinerTree.stats",
    "gds.beta.steinerTree.stream",
    "gds.beta.steinerTree.write",
    "gds.betweenness.mutate",
    "gds.betweenness.mutate.estimate",
    "gds.betweenness.stats",
    "gds.betweenness.stats.estimate",
    "gds.betweenness.stream",
    "gds.betweenness.stream.estimate",
    "gds.betweenness.write",
    "gds.betweenness.write.estimate",
    "gds.bfs.mutate",
    "gds.bfs.mutate.estimate",
    "gds.bfs.stats",
    "gds.bfs.stats.estimate",
    "gds.bfs.stream",
    "gds.bfs.stream.estimate",
    "gds.debug.sysInfo",
    "gds.degree.mutate",
    "gds.degree.mutate.estimate",
    "gds.degree.stats",
    "gds.degree.stats.estimate",
    "gds.degree.stream",
    "gds.degree.stream.estimate",
    "gds.degree.write",
    "gds.degree.write.estimate",
    "gds.dfs.mutate",
    "gds.dfs.mutate.estimate",
    "gds.dfs.stream",
    "gds.dfs.stream.estimate",
    "gds.eigenvector.mutate",
    "gds.eigenvector.mutate.estimate",
    "gds.eigenvector.stats",
    "gds.eigenvector.stats.estimate",
    "gds.eigenvector.stream",
    "gds.eigenvector.stream.estimate",
    "gds.eigenvector.write",
    "gds.eigenvector.write.estimate",
    "gds.fastRP.mutate",
    "gds.fastRP.mutate.estimate",
    "gds.fastRP.stats",
    "gds.fastRP.stats.estimate",
    "gds.fastRP.stream",
    "gds.fastRP.stream.estimate",
    "gds.fastRP.write",
    "gds.fastRP.write.estimate",
    "gds.graph.deleteRelationships",
    "gds.graph.drop",
    "gds.graph.exists",
    "gds.graph.export",
    "gds.graph.list",
    "gds.graph.nodeProperties.drop",
    "gds.graph.nodeProperties.stream",
    "gds.graph.nodeProperties.write",
    "gds.graph.nodeProperty.stream",
    "gds.graph.project",
    "gds.graph.project.cypher",
    "gds.graph.project.cypher.estimate",
    "gds.graph.project.estimate",
    "gds.graph.relationship.write",
    "gds.graph.relationshipProperties.stream",
    "gds.graph.relationshipProperty.stream",
    "gds.graph.relationships.drop",
    "gds.graph.removeNodeProperties",
    "gds.graph.sample.rwr",
    "gds.graph.sample.cnarw",
    "gds.graph.sample.cnarw.estimate",
    "gds.graph.streamNodeProperties",
    "gds.graph.streamNodeProperty",
    "gds.graph.streamRelationshipProperties",
    "gds.graph.streamRelationshipProperty",
    "gds.graph.writeNodeProperties",
    "gds.graph.writeRelationship",
    "gds.knn.mutate",
    "gds.knn.mutate.estimate",
    "gds.knn.stats",
    "gds.knn.stats.estimate",
    "gds.knn.stream",
    "gds.knn.stream.estimate",
    "gds.knn.write",
    "gds.knn.write.estimate",
    "gds.labelPropagation.mutate",
    "gds.labelPropagation.mutate.estimate",
    "gds.labelPropagation.stats",
    "gds.labelPropagation.stats.estimate",
    "gds.labelPropagation.stream",
    "gds.labelPropagation.stream.estimate",
    "gds.labelPropagation.write",
    "gds.labelPropagation.write.estimate",
    "gds.localClusteringCoefficient.mutate",
    "gds.localClusteringCoefficient.mutate.estimate",
    "gds.localClusteringCoefficient.stats",
    "gds.localClusteringCoefficient.stats.estimate",
    "gds.localClusteringCoefficient.stream",
    "gds.localClusteringCoefficient.stream.estimate",
    "gds.localClusteringCoefficient.write",
    "gds.localClusteringCoefficient.write.estimate",
    "gds.louvain.mutate",
    "gds.louvain.mutate.estimate",
    "gds.louvain.stats",
    "gds.louvain.stats.estimate",
    "gds.louvain.stream",
    "gds.louvain.stream.estimate",
    "gds.louvain.write",
    "gds.louvain.write.estimate",
    "gds.nodeSimilarity.mutate",
    "gds.nodeSimilarity.mutate.estimate",
    "gds.nodeSimilarity.stats",
    "gds.nodeSimilarity.stats.estimate",
    "gds.nodeSimilarity.stream",
    "gds.nodeSimilarity.stream.estimate",
    "gds.nodeSimilarity.write",
    "gds.nodeSimilarity.write.estimate",
    "gds.pageRank.mutate",
    "gds.pageRank.mutate.estimate",
    "gds.pageRank.stats",
    "gds.pageRank.stats.estimate",
    "gds.pageRank.stream",
    "gds.pageRank.stream.estimate",
    "gds.pageRank.write",
    "gds.pageRank.write.estimate",
    "gds.randomWalk.stats",
    "gds.randomWalk.stats.estimate",
    "gds.randomWalk.stream",
    "gds.randomWalk.stream.estimate",
    "gds.shortestPath.astar.mutate",
    "gds.shortestPath.astar.mutate.estimate",
    "gds.shortestPath.astar.stream",
    "gds.shortestPath.astar.stream.estimate",
    "gds.shortestPath.astar.write",
    "gds.shortestPath.astar.write.estimate",
    "gds.shortestPath.dijkstra.mutate",
    "gds.shortestPath.dijkstra.mutate.estimate",
    "gds.shortestPath.dijkstra.stream",
    "gds.shortestPath.dijkstra.stream.estimate",
    "gds.shortestPath.dijkstra.write",
    "gds.shortestPath.dijkstra.write.estimate",
    "gds.shortestPath.yens.mutate",
    "gds.shortestPath.yens.mutate.estimate",
    "gds.shortestPath.yens.stream",
    "gds.shortestPath.yens.stream.estimate",
    "gds.shortestPath.yens.write",
    "gds.shortestPath.yens.write.estimate",
    "gds.triangleCount.mutate",
    "gds.triangleCount.mutate.estimate",
    "gds.triangleCount.stats",
    "gds.triangleCount.stats.estimate",
    "gds.triangleCount.stream",
    "gds.triangleCount.stream.estimate",
    "gds.triangleCount.write",
    "gds.triangleCount.write.estimate",
    "gds.wcc.mutate",
    "gds.wcc.mutate.estimate",
    "gds.wcc.stats",
    "gds.wcc.stats.estimate",
    "gds.wcc.stream",
    "gds.wcc.stream.estimate",
    "gds.wcc.write",
    "gds.wcc.write.estimate",
    "gds.alpha.graph.project",
    "gds.alpha.linkprediction.adamicAdar",
    "gds.alpha.linkprediction.commonNeighbors",
    "gds.alpha.linkprediction.preferentialAttachment",
    "gds.alpha.linkprediction.resourceAllocation",
    "gds.alpha.linkprediction.sameCommunity",
    "gds.alpha.linkprediction.totalNeighbors",
    "gds.alpha.ml.oneHotEncoding",
    "gds.graph.exists",
    "gds.similarity.cosine",
    "gds.similarity.euclidean",
    "gds.similarity.euclideanDistance",
    "gds.similarity.jaccard",
    "gds.similarity.overlap",
    "gds.similarity.pearson",
    "gds.util.NaN",
    "gds.util.asNode",
    "gds.util.asNodes",
    "gds.util.infinity",
    "gds.util.isFinite",
    "gds.util.isInfinite",
    "gds.util.nodeProperty",
    "gds.version",
]
